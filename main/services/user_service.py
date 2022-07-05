import json
import os

from main.dto import User
import requests


class UserService:
    def __init__(self):
        self.url = os.getenv('API_URL')

    def create(self, user: User) -> User:
        r = requests.post(self.url + '/api/v1/users', json=user)
        # TODO: verificar 200 y devolver algo
        return user

    def find_by_username(self, username: str) -> str:
        data = {}
        r = requests.get(self.url + '/api/v1/users/username/' + username, json=data)
        # TODO: verificar 200 y devolver algo
        return json.loads(r.text)['key']

    def find_by_id(self, id):
        r = requests.get(self.url + '/api/v1/users/id/' + id)
        # TODO: verificar 200 y devolver algo
        return id

    def find_all(self):
        r = requests.get(self.url + '/api/v1/users/all')
        # TODO: verificar 200 y devolver algo
        return r.status_code

    def update(self, user: User) -> User:
        r = requests.put(self.url + '/api/v1/users/update', json=user)
        # TODO: verificar 200 y devolver algo
        return user
