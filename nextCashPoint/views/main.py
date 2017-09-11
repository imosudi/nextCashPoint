from flask import Blueprint, render_template, url_for
from datetime import datetime

bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/')
def index():
   return render_templates('index.html', current_time=datetime.utcnow())
