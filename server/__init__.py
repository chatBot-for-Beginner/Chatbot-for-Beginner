from flask import Flask
import config

#어플리케이션 팩토리 : 애플리케이션 팩토리는 쉽게 말해 app 객체를 생성하는 함수를 의미한다.

def create_app():
    app = Flask(__name__)
    
    from .api import api
    app.register_blueprint(api.bp)
    return app