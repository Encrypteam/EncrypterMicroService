from flask import Flask
from dotenv import load_dotenv
from flask_consulate import Consul

consul = Consul()


def create_app():
    app = Flask(__name__)
    consul.init_app(app)
    consul.register_service(
        name='encrypter-ms',
        interval='10s',
        tags=[''],
        httpcheck='https://encrypter.encrypteam.localhost/healthcheck'
    )
    load_dotenv()

    from main.resources import resource_enc, home
    app.register_blueprint(resource_enc, url_prefix='/api/v1')
    app.register_blueprint(home, url_prefix='/')
    return app
