import os

from main.dto import User
import requests


class UserService:
    def __init__(self):
        self.url = os.getenv('API_USER_URL')

    def create(self, user: User) -> User:
        r = requests.post(self.url + '/api/v1/users', json=user)
        # TODO: verificar 200 y devolver algo
        return user

    def find_by_username(self, username: str) -> User:
        r = requests.get(self.url + '/api/v1/users/username/' + username)
        # TODO: verificar 200 y devolver algo
        return r.status_code

    def find_by_id(self, id):
        r = requests.get(self.url + '/api/v1/users/id/' + id)
        # TODO: verificar 200 y devolver algo
        return r.status_code

    def find_all(self):
        r = requests.get(self.url + '/api/v1/users/all')
        # TODO: verificar 200 y devolver algo
        return r.status_code

    def update(self, user: User) -> User:
        r = requests.put(self.url + '/api/v1/users/update', json=user)
        # TODO: verificar 200 y devolver algo
        return r.status_code

