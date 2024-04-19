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

from .routes import UsersRouter
from .routes.LoginRouter import login_routes
from flask_cors import CORS
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
# app = Flask(__name__)
# CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:5174"}})
def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(UsersRouter.main, url_prefix='/adminpage')
    app.register_blueprint(login_routes)
    print(app.url_map)
    return app