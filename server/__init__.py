import os
from flask import (
  Flask, Blueprint, send_from_directory, session, g
)
from flask_json import FlaskJSON
from flask_migrate import Migrate

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
  from .db.connection import db
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("POSTGRES_URI")
  db.init_app(app)
  migrate = Migrate(app, db)

  # JSON ENCODING
  json = FlaskJSON(app)

  # serving built frontend
  @app.get('/')
  def home():
      return send_from_directory('static', 'index.html')

  @app.get('/<path:path>')
  def static_files(path):
      return send_from_directory('static', path)

  from .routes import auth
  from .routes import artwork

  api = Blueprint('api', __name__, url_prefix='/api')

  # @api.before_app_request
  # def load_logged_in_user():
  #     user_id = session.get('user_id')

  #     if user_id is None:
  #         g.user = None
  #     else:
  #         g.user = mongo.db.users.find_one({'_id': user_id})

  api.register_blueprint(auth.bp)
  api.register_blueprint(artwork.bp)
  app.register_blueprint(api)

  return app