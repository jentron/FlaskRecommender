# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:19:48 2020

@author: rjensen
"""
import numpy as np
from collections import OrderedDict
from app.db import get_db
#from timeit import default_timer as timer


def jaccard_similarity(movie_ids, desired_ids):
    """    movie_ids is all the movies to test against
    desired_ids is the selected movies
    """
#    start = timer()
    db = get_db()
    
    genres = db.execute('SELECT genre_id, count(*)  FROM movie_genres WHERE movie_id IN (%s) group by genre_id' % ','.join('?'*len(desired_ids)), desired_ids).fetchall()
    
    # build a dictionary
    c = {'total': 0}
    for k, v in genres:
        c[k] = v
        c['total'] += v
        
    result = {}
    for movie_id in movie_ids:
        #calculate similiarity, save in a dictionary keyed on movie_id
        numerator = 0
        denomenator = c['total']
    
        b = db.execute('SELECT genre_id  FROM movie_genres WHERE movie_id = ?;', (movie_id,)).fetchall()

        for genre in b:
            if genre[0] in c:
                numerator += c[genre[0]]
                #print('\n\nNumerator = ' + str(numerator))
                #print('Denominator = ' + str(denomenator))
                
        similarity = numerator / denomenator
        result[movie_id] = similarity
    
#    end = timer()
#    print("Processed " + str(len(movie_ids)) + " movies in " +str( end-start))
    # https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key#9001529
    return OrderedDict(sorted(result.items(), reverse=True, key=lambda t: t[1]))

# create and instance of the IMDb class
from imdb import IMDb

def imdb_update_poster(movie_id):
    ia = IMDb()
    db = get_db()
    
    movie=db.execute('select * from movies where movie_id = ?;', (movie_id,)).fetchone()
    if movie['imdb_poster'] is None:
        the_movie = ia.get_movie(movie['imdb_id'])
        db.execute('''update movies set imdb_poster = ?, imdb_rating = ?
        where movie_id = ?;''', (the_movie['cover url'], the_movie['rating'], movie['movie_id']))
        # get imdb_poster url and imdb_rating from imdb
        # write imdb_poster url and imdb_rating to database
        db.commit()
        movie = db.execute('select * from movies where movie_id = ?;', (movie['movie_id'],)).fetchone()

    return(movie['imdb_poster'])

