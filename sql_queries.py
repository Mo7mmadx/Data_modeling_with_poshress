

# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


#Create 



user_table_create = ("""CREATE TABLE IF NOT EXISTS users ( 
user_id text NOT NULL, 
first_name text NOT NULL , 
last_name text   , 
gender text ,
level text  ,
PRIMARY KEY (user_id))
""")



song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
song_id text  NULL ,
title text NOT NULL, 
artist_id text NOT NULL, 
year int NOT NULL,
duration float NOT NULL  ,
PRIMARY KEY (song_id) )
""")



artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
artist_id text NOT NULL , 
name text NOT NULL , 
location text   ,
lattitude text  ,
longitude text  ,
PRIMARY KEY (artist_id) )
""")


time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
start_time timestamp NOT NULL ,
hour int NOT NULL ,
day int NOT NULL ,
week int NOT NULL , 
month int NOT NULL, 
year int NOT NULL,
weekday text NOT NULL ,
PRIMARY KEY (start_time) ) 
""")


songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays ( 
songplay_id SERIAL NOT NULL,  
start_time timestamp  NOT NULL, 
user_id text REFERENCES users(user_id) , 
level text NOT NULL, 
song_id text REFERENCES songs(song_id)   ,
artist_id text REFERENCES artists(artist_id)   ,
session_id int  NOT NULL ,
location text NOT NULL ,
user_agent text NOT NULL ,
PRIMARY KEY (songplay_id))
""")




# INSERT RECORDS


songplay_table_insert = ("""INSERT INTO songplays (
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")


user_table_insert = (""" INSERT INTO users (
user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET first_name=users.first_name, last_name=users.last_name, gender=users.gender, level=users.level

""")

song_table_insert = ("""INSERT INTO songs (
song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE SET title=songs.title, artist_id=songs.artist_id,year=songs.year, duration=songs.duration
""")


artist_table_insert = (""" INSERT INTO artists (
artist_id, name, location, lattitude, longitude) 
VALUES (%s, %s, %s, %s, %s) 
ON CONFLICT (artist_id) DO UPDATE SET name=artists.name, location=artists.location, lattitude=artists.lattitude,longitude=artists.longitude 
""")



time_table_insert = (""" INSERT INTO time (
start_time, hour, day, week, month, year, weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT (start_time) DO UPDATE SET hour=time.hour, day=time.day, week=time.week, month=time.month, 
year=time.year, weekday=time.weekday
""")


#song_select 

song_select = "SELECT songs.song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title = %s AND artists.name=%s AND songs.duration=%s" 



# QUERY LISTS

create_table_queries = [ user_table_create, song_table_create, artist_table_create, time_table_create , songplay_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]