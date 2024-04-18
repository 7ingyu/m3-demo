import functools

from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_json import json_response

from ..db.connection import db
from ..db.models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.post('/register')
def register():
  req = request.get_json()
  username = req['username']
  password = req['password']
  error = None

  if not username:
    error = 'Username is required.'
  elif not password:
    error = 'Password is required.'

  if error is None:
    user = db.session.execute(
      db
        .select(User)
        .where(User.username == username)
    ).scalar()
    print(user)
    # mongo.db.users.find_one({
    #   'username': username,
    # })
    if user is None:
      user = User(
          username=username,
          password=generate_password_hash(password),
      )
      db.session.add(user)
      db.session.commit()
      session.clear()
      session['user_id'] = user.id
      return json_response(id=user.id, status=201)
    else:
      error = f"User {username} is already registered."
      return json_response(error=error, status=400)
  flash(error)

# TO DO: Implement login
@bp.post('/login')
def login():
  username = request.form['username']
  password = request.form['password']
  error = None
  # user = mongo.db.findOne({
  #   'username': username,
  # })
  user = None

  if user is None:
    error = 'Incorrect username.'
  elif not check_password_hash(user['password'], password):
    error = 'Incorrect password.'

  if error is None:
    # Login success
    # TODO: Convert to JSON response
    # Also figure out how to add to session
    session.clear()
    session['user_id'] = user['id']
    return redirect(url_for('index'))

  flash(error)

@bp.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect('/register')

        return view(**kwargs)

    return wrapped_view