from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
