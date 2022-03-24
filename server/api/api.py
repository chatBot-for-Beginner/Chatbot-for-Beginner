from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello():
    return 'hello flask'

@bp.route('/hello/api')
def hello_api():
    return 'hello api'