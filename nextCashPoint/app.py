from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


from nextCashPoint.views.main import bp as index_bp


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.register_blueprint(index_bp)




