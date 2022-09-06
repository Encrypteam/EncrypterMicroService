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
    consul.apply_remote_config(namespace='configuration/encrypter/')
    load_dotenv()

    print("CONFIG DE CONSUL", app.config['encrypter']['API_URL'])
    from main.resources import resource_enc, home
    app.register_blueprint(resource_enc, url_prefix='/api/v1')
    app.register_blueprint(home, url_prefix='/')
    return app
