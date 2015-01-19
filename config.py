import os
class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']
    BASE_URL = os.environ['BASE_URL']
    WWW_BASE_URL = os.environ['WWW_BASE_URL']
    ALLOWED_DOMAINS = os.environ['ALLOWED_DOMAINS']
    REDISCLOUD_URL = os.environ['REDISCLOUD_URL']

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(DevelopmentConfig):
    TESTING = True

