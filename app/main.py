from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from app.auth import login_required
from app.db import get_db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    db = get_db()
    movies = db.execute(
     'SELECT * FROM movies ORDER BY RANDOM() LIMIT 10;'
    ).fetchall()
    return render_template('main/index.html', movies=movies, title='Random Movies')

@bp.route('/search', methods=('GET', 'POST'))
def search():
    return render_template('main/index.html', movies=movies, title='Search For Movies')


@bp.route('/selected', methods=('GET', 'POST'))
## @login_required
def selected():
    selected=request.cookies.get('selected')
    
    if selected is None:
      return render_template('main/index.html', movies="", title='No Selected Movies')

    db = get_db()
    movies = db.execute(
     'SELECT * FROM movies where movie_id in ('+selected+') ORDER BY title LIMIT 10 ;').fetchall()
    return render_template('main/index.html', movies=movies, title='Selected Movies')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.post_id, title, body, created, p.user_id, username'
        ' FROM posts p JOIN users u ON p.user_id = u.user_id'
        ' WHERE p.post_id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['user_id'] != g.user['user_id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
##@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE posts SET title = ?, body = ?'
                ' WHERE post_id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('main/update.html', post=post)

@bp.route('/cookie', methods=('POST','GET'))
#@login_required
def cookies():

    return redirect(url_for('main.index'))

@bp.route('/favicon.ico', methods=('POST','GET'))
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))
