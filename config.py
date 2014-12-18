import os
class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ['SECRET_KEY']
    BASE_URL = os.environ['BASE_URL']
    WWW_BASE_URL = os.environ['WWW_BASE_URL']
    ALLOWED_DOMAINS = os.environ['ALLOWED_DOMAINS']

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(DevelopmentConfig):
    TESTING = True
