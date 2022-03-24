import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'server.db')) # 데이터베이스 접근하는 url
SQLALCHEMY_TRACK_MODIFICATIONS = False