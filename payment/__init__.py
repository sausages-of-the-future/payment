import os
from flask import Flask
import redis

#app
app = Flask(__name__)
app.config.from_object(os.environ.get('SETTINGS'))

from messenger import Connector
connector = Connector(app)

from payment import views
