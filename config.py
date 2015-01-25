import os


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("EXCHANGE_SECRET")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = False
    DEVELOPMENT = True
    SECRET_KEY = "a8814636fe767d1fbe7160dccbf35ee9238bc135add24c7256c360fb288ab22b4e78026a469ebb50336d7794d7864dc9ea0d95f58a8707efabaa34c7d0c6d5df9ca4deb4de3742c9d43b3016673fcb58"
