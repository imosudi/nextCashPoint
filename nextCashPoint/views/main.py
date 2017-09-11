from flask import Blueprint, render_template, url_for

bp = Blueprint(__name__, __name__,template_folder='templates')

@bp.route('/')
def index():
   return "Hello world!"
