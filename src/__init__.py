from flask import Flask
from flask_cors import CORS


from .routes import UsersRouter
from .routes import ArtRouter
from .routes.LoginRouter import login_routes

app = Flask(__name__)


CORS(app)


def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'  
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


app.after_request(add_cors_headers)


def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(UsersRouter.main, url_prefix='/adminpage')
    app.register_blueprint(ArtRouter.main, url_prefix='/personalgallery')
    app.register_blueprint(login_routes)
    return app