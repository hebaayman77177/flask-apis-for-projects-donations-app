class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://heba5:123456789@127.0.0.1:3306/flask"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = "JWT-SECRET"
    SECRET_KEY = "SECRET-KEY"
    SECURITY_PASSWORD_SALT = "SECRET-KEY-PASSWORD"


class DevelopmentConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://heba5:123456789@127.0.0.1:3306/flask3"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = "JWT-SECRET"
    SECRET_KEY = "SECRET-KEY"
    SECURITY_PASSWORD_SALT = "SECRET-KEY-PASSWORD"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://heba5:123456789@127.0.0.1:3306/flask"
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = "JWT-SECRET"
    SECRET_KEY = "SECRET-KEY"
    SECURITY_PASSWORD_SALT = "SECRET-KEY-PASSWORD"
