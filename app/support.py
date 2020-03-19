# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:19:48 2020

@author: rjensen
"""
import numpy as np
from collections import OrderedDict

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

def imdb_update(movies):
    """    update (if required) the imdb_poster url and imdb_rating
    note: if imdb_poster url is non-null, both url and imdb_rating are assumed good
    """
    for movie in movies:
        if movie['imdb_poster'] is None:
            pass
            # get imdb_poster url and imdb_rating from imdb
            # write imdb_poster url and imdb_rating to database
    
    return (movies)