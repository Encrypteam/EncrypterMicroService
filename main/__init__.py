from flask import Flask
from dotenv import load_dotenv
from flask_consulate import Consul
from prometheus_flask_exporter import PrometheusMetrics
import logging
import logstash




logger = logging.getLogger("python-logstash-logger")
logger.setLevel(logging.DEBUG)

logger.addHandler(logstash.TCPLogstashHandler('127.0.0.1', 5059, version = 1))

consul = Consul(max_tries=25)
metrics = PrometheusMetrics.for_app_factory()
metrics.info('encrypter', 'Description', version='0.1')

def create_app():
    app = Flask(__name__)
    metrics.init_app(app)
    consul.init_app(app)
    consul.register_service(
        name='encrypter-ms',
        interval='10s',
        tags=['encrypter'],
        httpcheck='https://encrypter.encrypteam.localhost/healthcheck'
    )
    consul.apply_remote_config(namespace='configuration/encrypter/')
    load_dotenv()

    print("CONFIG DE CONSUL", app.config['encrypter']['API_URL'])
    from main.resources import encrypter, home
    app.register_blueprint(encrypter, url_prefix='/api/v1')
    app.register_blueprint(home, url_prefix='/')
    return app
