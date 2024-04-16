import os
from flask import (
  Flask, Blueprint
)
from flask_pymongo import PyMongo
from flask_json import FlaskJSON

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # DATABASE
  app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
  mongo = PyMongo(app)

  # JSON ENCODING
  json = FlaskJSON(app)

  # a simple page that says hello
  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  from .routes import auth

  api = Blueprint('api', __name__, url_prefix='/api')
  api.register_blueprint(auth.bp)
  app.register_blueprint(api)

  return app