import json
import os


from main.dto import User
import requests
import consulate



class UserService:
    def __init__(self):
        session = consulate.Consul()
        session.kv['tato'] = dict({'API_URL': os.getenv('API_URL')})
        self.url = os.getenv('API_URL')

    def create(self, user: User) -> User:
        data = {'username': user.user_name, 'email': user.email}
        r = requests.post(self.url + '/api/v1/users', json=data)
        # TODO: verificar 200 y devolver algo
        return r.status_code

    def find_by_username(self, username):
        data = {}
        r = requests.get(self.url + '/api/v1/users/username/' + username, json=data)
        # TODO: verificar 200 y devolver algo
        if r.status_code == 200:
            return json.loads(r.text)['key']
        else:
            return None

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
