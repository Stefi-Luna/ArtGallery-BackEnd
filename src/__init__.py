from flask import Flask
from flask_cors import CORS

# Importar los blueprints
from .routes import UsersRouter
from .routes import ArtRouter
from .routes.LoginRouter import login_routes

app = Flask(__name__)

# Configurar CORS para permitir solicitudes desde cualquier origen
CORS(app)

# Registrar los blueprints
def init_app(config):
    app.config.from_object(config)
    app.register_blueprint(UsersRouter.main, url_prefix='/adminpage')
    app.register_blueprint(ArtRouter.main, url_prefix='/personalgallery')
    app.register_blueprint(login_routes)
    return app