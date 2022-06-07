from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    load_dotenv()

    from main.resources import resource_enc, home

    app.register_blueprint(resource_enc, url_prefix='/api/v1')
    app.register_blueprint(home, url_prefix='/api/v1')
    return app
