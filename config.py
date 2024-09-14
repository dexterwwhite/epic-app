class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'
    DATABASE_URI = 'sqlite:///example.db'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    CONFIG_VARIABLE = 'This is a fun and goofy config variable because this is the development environment!'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    CONFIG_VARIABLE = 'This is a very serious config variable. We\'re in a production environment now, kiddo.'