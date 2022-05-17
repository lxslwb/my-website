from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.db import get_db

bp = Blueprint('introduction', __name__, url_prefix='/introduction')


@bp.route('/my')
def my():
    db = get_db()
    posts = db.execute(
        'SELECT body FROM my'
    ).fetchall()
    return render_template('introduction/my.html', posts=posts)
