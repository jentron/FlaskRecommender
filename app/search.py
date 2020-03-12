from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from app.auth import login_required
from app.db import get_db

bp = Blueprint('search', __name__)


@bp.route('/search', methods=('GET', 'POST'))
def search():
    movies=""
    if request.method == 'POST':
        sss = request.form['titlewords']
        db = get_db()
        movies = db.execute(
            'SELECT * FROM movies WHERE title like ?', ("%Toy%",)
        ).fetchall()


    return render_template('main/search.html', movies=movies, title='Search For Movies')

