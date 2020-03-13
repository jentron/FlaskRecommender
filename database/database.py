# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:36:35 2020

@author: rjensen
"""
import pandas as pd
import numpy  as np
import re
import sqlite3
from flask import Flask
app = Flask(__name__)

DATABASE = 'movie1.db'

conn = sqlite3.connect(DATABASE)

movie_db = pd.read_csv("movies.csv")

#%% Create the database
with app.app_context():
    with app.open_resource('movies_db_ddl.sql', mode='r') as f:
        conn.executescript(f.read())
        conn.commit()

#%% populate the movies table

count = 0
for index, movie in movie_db.iterrows():
    title = re.sub(r'^(.*?)\s*\(([1-2][0-9]{3})\)\s*$',r'\1',movie.title)
    year  = re.sub(r'^(.*)\(([1-2][0-9]{3})\)\s*$',r'\2',movie.title)
#    conn.execute(f"INSERT INTO movies (movie_id,title,year,imdb_id) \
#      VALUES ({movie.movieId}, '{title}', {year}, {movie.imdbId});")
    conn.execute("INSERT INTO movies (movie_id,title,year,imdb_id) \
      VALUES (?, ?, ?, ?);", (movie.movieId, title, year, movie.imdbId))
    count += 1
##    if (count > 10):
##        break

conn.commit()
print (f"{count} Movie Records created successfully")

#%% 
count = 0
genre_count = 0
for index, row in movie_db.iterrows():
    genres = row.genres.split('|')
    for g in genres:
        while True:
            cur = conn.execute("select genre_id from genres where label = ?;",(g,))
            genre_id = cur.fetchone()
        
            if(genre_id is None ):
                conn.execute("insert into genres (label) values (?) ", (g,))
                conn.commit()
                genre_count += 1
                
            if (genre_id is not None):
                break
            
        # print(bob)
        conn.execute("insert into movie_genres (movie_id, genre_id) values (?, ?)", (row.movieId, genre_id[0]))
        count += 1

#    count += 1
#    if (count > 4):
#        break

conn.commit()
print(f"Inserted {genre_count} genres and {count} unique records.")


conn.close()
