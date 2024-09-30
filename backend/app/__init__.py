from flask import Flask
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from .routes import blueprints

def createApp(configClass=DevelopmentConfig):

    # Loads db env vars and whatever else
    load_dotenv()

    # Run dat shi
    app = Flask(__name__)
    app.config.from_object(configClass)

    for bp in blueprints:
        app.register_blueprint(bp)

    return app