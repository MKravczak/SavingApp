import os

class Config:
    SECRET_KEY = os.environ('SECRET_KEY','sektretny_klucz')
    SQLALCHEMY_DATABASE_URI = os.environ('DATABASE_URL','sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False