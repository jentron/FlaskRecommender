from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from app.auth import login_required
from app.db import get_db

bp = Blueprint('recommend', __name__)


@bp.route('/recommend')
def recommend():
    desired_ids = request.cookies.get("selected").split(",") #all selected movie_ids in a list
    
    db = get_db()
    movies = db.execute('SELECT * FROM movies WHERE movie_id IN (%s) order by title' %
                           ','.join('?'*len(desired_ids)), desired_ids).fetchall()

    return render_template('main/index.html', movies=movies, title='Recommended for You: '+','.join(str(e) for e in desired_ids))

