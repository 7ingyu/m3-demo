import functools

from flask import (
    Blueprint, flash, g, redirect, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_json import json_response

from ..db.connection import mongo

bp = Blueprint('artwork', __name__, url_prefix='/artwork')

def encode_artwork (artwork):
  data = {
    'id': str(artwork.id),
    'title': artwork.title,
    'price': artwork.price,
    'artist': encode_artist(artwork.artist),
  }

def encode_artist (artist):
  data = {
    'id': str(artist.id),
    'name': artist.name,
  }

@bp.get('/all')
def all():
  artworks = mongo.db.artworks.find()
  res = [encode_artwork(a) for a in list(artworks)]
  return json_response(artworks=res)

@bp.post('/')
def create():
  req = request.get_json()
  mongo.db.users.insert_one({
    'title': req['title'],
    'price': req['price'],
    'artist': req['artist'],
  })
  return json_response(status=201)