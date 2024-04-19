class DevelopmentConfig():
    DEBUG = True

config={
    'development': DevelopmentConfig
}

import secrets
class Config:
    DEBUG = False
    SECRET_KEY = secrets.token_hex(32)  # Genera una clave secreta aleatoria
class DevelopmentConfig(Config):
    DEBUG = True