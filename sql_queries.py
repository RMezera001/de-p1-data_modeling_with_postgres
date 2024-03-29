# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
songplay_id SERIAL PRIMARY KEY, 
start_time varchar NOT NULL, 
user_id varchar NOT NULL, 
level varchar, 
song_id varchar NOT NULL, 
artist_id varchar NOT NULL, 
session_id varchar NOT NULL, 
location varchar, 
user_agent varchar NOT NULL
);""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id varchar PRIMARY KEY, 
first_name varchar NOT NULL, 
last_name varchar NOT NULL, 
gender char, 
level varchar
);""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id varchar PRIMARY KEY, 
title varchar NOT NULL, 
artist_id varchar NOT NULL, 
year int, 
duration numeric NOT NULL
);""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id varchar PRIMARY KEY, 
artist_name varchar NOT NULL, 
artist_location varchar, 
artist_latitude varchar, 
artist_longitude varchar
);""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time numeric PRIMARY KEY, 
hour numeric NOT NULL, 
day int NOT NULL, 
week int NOT NULL, 
month int NOT NULL, 
year int NOT NULL, 
weekday int NOT NULL
);""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (
start_time, user_id, level, 
song_id, artist_id, session_id, location, 
user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (
user_id, first_name, last_name, 
gender, level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
""")

song_table_insert = ("""
INSERT INTO songs (
song_id,title,artist_id,year,duration) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (
artist_id,artist_name,artist_location,
artist_latitude,artist_longitude) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT(artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (
start_time, hour, day, 
week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT songs.title, artists.artist_name FROM (
songs JOIN artists ON 
songs.artist_id = artists.artist_id) 
WHERE (songs.title = %s 
AND artists.artist_name = %s 
AND songs.duration = %s
);""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]