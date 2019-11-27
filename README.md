# Data Modeling with Postgres
In this project, we'll apply data modeling with Postgres and build an ETL pipeline using Python. We will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL. 

#### Fact Table
- songplays - records in log data associated with song plays i.e. records with page NextSong
    - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
    
#### Dimension Tables

- users - users in the app
    - user_id, first_name, last_name, gender, level
- songs - songs in music database
    - song_id, title, artist_id, year, duration
- artists - artists in music database
    - artist_id, name, location, latitude, longitude
- time - timestamps of records in songplays broken down into specific units
    - start_time, hour, day, week, month, year, weekday

## Usage

- In the terminal use `python create_tables.py` to create tables.  This must be done before running `etl.py`, `etl.ipynb`, or `test.ipynb`
- In the terminal use `etl.py` to insert data into the tables from `log_data` and `song_data`.
- After running `etl.py` use `test.ipynb` to check the results.
- If you run `test.ipynb` or `etl.ipynb`, you will need to restart the kernal to run other programs.
- Run `create_tables.py` to clear the tables and start over.


## Files

- data: Contains log_data and song_data.
- etl.ipynp: Notebook that goes through the process of creating the ETL inserting data into the tables created
- test.ipynb: Notebook to test if tables are created and data is inserted correctly into tables.
- create_tables.py: Creates sparkifydb tables for data to be inserted into.
- etl.py: reads and processes files from song_data and log_data and loads them into tables.
- sql.queries.py:  Contains all queries, insert and create statements.


###### Author

Ryan Mezera