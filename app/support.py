# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:19:48 2020

@author: rjensen
"""
import numpy as np
from collections import OrderedDict
from app.db import get_db

def jaccard_similarity(movie_ids, desired_ids):
    """    movie_ids is all the movies to test against
    desired_ids is the selected movies
    """
    dict = {}
    for movie_id in movie_ids:
        #calculate similiarity, save in a dictionary keyed on movie_id
        similarity = np.random.rand() # FIXME:
        dict[movie_id] = similarity
        

    # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key#9001529
    return OrderedDict(sorted(dict.items(), reverse=True, key=lambda t: t[1]))

# create and instance of the IMDb class
from imdb import IMDb

def imdb_update(movies):
    """    update (if required) the imdb_poster url and imdb_rating
    note: if imdb_poster url is non-null, both url and imdb_rating are assumed good
    """
    ia = IMDb()
    db = get_db()

# had to play with indexes because movies is a list of tuples
# and they are immutable
    #for movie in movies: 
    for index in range(len(movies)):
        movie=movies[index]
        if movie['imdb_poster'] is None:
            the_movie = ia.get_movie(movie['imdb_id'])
            db.execute('''update movies set imdb_poster = ?, imdb_rating = ?
            where movie_id = ?;''', (the_movie['cover url'], the_movie['rating'], movie['movie_id']))
            # get imdb_poster url and imdb_rating from imdb
            # write imdb_poster url and imdb_rating to database
            db.commit()
            movies[index] = db.execute('select * from movies where movie_id = ?;', (movie['movie_id'],)).fetchone()

#            movie['imdb_poster'] = the_movie['cover url']
#            movie['imdb_rating'] = the_movie['rating']

    
    return (movies)