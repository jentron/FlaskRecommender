from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from app.auth import login_required
from app.db import get_db
from app.support import jaccard_similarity

bp = Blueprint('recommend', __name__)


@bp.route('/recommend')
def recommend():
    desired_ids = request.cookies.get("selected").split(",") #all selected movie_ids in a list
    
    db = get_db()
    movie_ids = db.execute('''
                           SELECT movie_id 
                           FROM movie_genres 
                           WHERE genre_id IN (
                           SELECT DISTINCT genre_id
                           FROM movie_genres
                           WHERE movie_id IN (%s))''' %
                           ','.join('?'*len(desired_ids)), desired_ids).fetchall()
                           
    movie_ids = [i[0] for i in movie_ids] # unpack tuples
    movie_ids = jaccard_similarity(movie_ids, desired_ids)
#    print(movie_ids)
    movie_ids = list(movie_ids.keys())[0:10]
   
    movies = db.execute('SELECT * FROM movies WHERE movie_id IN (%s) order by title' % 
                        ','.join('?'*len(movie_ids)), movie_ids).fetchall()

    return render_template('main/index.html', movies=movies, title='Recommended for You: '+','.join(str(e) for e in desired_ids))

