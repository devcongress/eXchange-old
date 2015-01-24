import os


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('EXCHANGE_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = False
    DEVELOPMENT = True
