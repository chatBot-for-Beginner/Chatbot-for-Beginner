from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

#어플리케이션 팩토리 : 애플리케이션 팩토리는 쉽게 말해 app 객체를 생성하는 함수를 의미한다.

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # orm 설정
    db.init_app(app)
    migrate.init_app(app,db)

    # 블루프린트
    from .api import api
    app.register_blueprint(api.bp)
    return app