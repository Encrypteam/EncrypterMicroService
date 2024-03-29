from crypt import methods

from flask import Blueprint, jsonify
from main import metrics

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    #logger.info("home")
    return jsonify('Welcome to encrypter microservice'), 200


@metrics.summary('request_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@home.route('/healthcheck')
def healthcheck():
    return jsonify({'status': 'up'}), 200


