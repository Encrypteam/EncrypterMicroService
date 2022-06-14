from flask import Blueprint, jsonify
import requests

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    return jsonify('Welcome to encrypter microservice'), 200
