from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from app.auth import login_required
from app.db import get_db
from app.support import imdb_update

bp = Blueprint('search', __name__)


@bp.route('/search', methods=('GET', 'POST'))
def search():
    movies=""
    words=""
    if request.method == 'POST':
        var = request.form['titlewords'].lower()
        words = var.split(" ")
        where = ""
        for word in words:
            where = where+"lower(TITLE) like '%"+word+"%' AND "
      
        where = where[:-5]
        sql="select * from movies where "+where+" ORDER BY RANDOM() LIMIT 10;"

        db = get_db()
        movies = db.execute(sql).fetchall()

    movies = imdb_update(movies)
    return render_template('main/search.html', movies=movies, words=words, title='Search For Movies')

