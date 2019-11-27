import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *



def process_song_file(cur, filepath):
    '''
    This function will create a song_table and artist_table using the song_data

    Input:
        - cur- psycopg2.connect().cursor()
        - filepath- filepath to song data
    Output: 
        Creates song_table and artist_table
    '''
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = list((df[['song_id','title','artist_id','year','duration']].values)[0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = list(df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values[0])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    This function will create a time_table, user_table, and songplay_table using the log_data

    Input:
        - cur- psycopg2.connect().cursor()
        - filepath- filepath to log data
    Output: 
        Creates song_table and artist_table
    '''
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'],unit='ms')
    
    #Extract the timestamp, hour, day, week of year, month, year, and weekday 
    timestamp = df['ts']/1000
    hour = t.dt.hour
    day = t.dt.day
    week_of_year = t.dt.date.apply(lambda x: str(x.isocalendar()[1]))
    month = t.dt.month
    year = t.dt.year
    weekday = t.dt.weekday
    
    # insert time data records
    time_data = (timestamp, hour, day, week_of_year, month, year, weekday)
    column_labels = ['timestamp', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday']
    time_df = pd.DataFrame({'timestamp':timestamp, 'hour':hour, 'day':day,'week_of_year':week_of_year,'month':month,'year':year,'weekday':weekday})

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)
        
    #Create index to be used in songplay_id
    df['index'] = df.index
    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results

        else:
            songid, artistid = None, None

        # Get Row based on songid and artistid
        tmp1 = df[df['artist'] == artistid]
        tmp2 = df[df['song'] == songid]

        # insert songplay record
        if tmp2.shape[0] > 0:
            print(tmp2)
            songplay_data = (tmp2[['ts','userId','level','song','artist','sessionId','location','userAgent']].values)[0]
            print(songplay_data)
            cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()