import os

class Config(object):
    DEBUG = False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{}:{}@{}/{}".format(os.getenv('SQLALCHEMY_DATABASE_USERNAME'), os.getenv('SQLALCHEMY_DATABASE_PASSWORD'), os.getenv('SQLALCHEMY_DATABASE_HOST'), os.getenv('SQLALCHEMY_DATABASE_DBNAME'))
    SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_POOL_SIZE=20
    SQLALCHEMY_POOL_TIMEOUT=30
    EXPTIME= os.getenv('EXP_TIME')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    TESTING = True