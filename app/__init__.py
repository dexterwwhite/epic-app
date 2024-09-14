from flask import Flask
from config import DevelopmentConfig, ProductionConfig

def createApp(configClass=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(configClass)

    from .routes import main
    app.register_blueprint(main)

    return app