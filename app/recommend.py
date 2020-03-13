from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from app.auth import login_required
from app.db import get_db

bp = Blueprint('recommend', __name__)


@bp.route('/recommend')
def recommend():
    cookie = request.cookies.get("selected").split(",") #all selected movie_ids in a list
    
    sql="select * from movies where title = 'Toy Story' ORDER BY RANDOM() LIMIT 10;"
    
    db = get_db()
    movies = db.execute(sql).fetchall()

    return render_template('main/index.html', movies=movies, title='Recommended for You')

