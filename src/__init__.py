from flask import Flask
from flask_cors import CORS

# Routes
from .routes import UsersRouter
from .routes import PaintingsRouter

# app = Flask(__name__)

# CORS(app, resources={"*": {"origins": "http://localhost:*"}})

app = Flask(__name__)
CORS(app, automatic_options=True)

def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(UsersRouter.main, url_prefix='/adminpage')
    app.register_blueprint(PaintingsRouter.main, url_prefix='/personalgallery')
    return app