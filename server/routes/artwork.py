import functools

from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_json import json_response

from ..db.connection import db
from ..db.models.artwork import Artwork

bp = Blueprint('artwork', __name__, url_prefix='/artwork')

@bp.get('/all')
def all():
  artworks = db.session.execute(
      db
        .select(Artwork)
    ).scalars()
  return json_response(artworks=[a.as_dict() for a in artworks])

@bp.post('/')
def create():
  req = request.get_json()
  # todo: validate request (remove anything that should not exist in the request)
  valid_keys = ['title', 'price', 'medium', 'artist']
  for key in req.keys():
    if key not in valid_keys:
      del req[key]
  # check that each key is the correct value type
  artwork = Artwork(**req)
  db.session.add(artwork)
  db.session.commit()
  return json_response(status=201)