from main.dto.user import User
from .user_service import UserService
from main.utils import Encrypter


class EncrypterService:
    def __init__(self):
        self.userService = UserService()
        self.encrypter = Encrypter()

    def key_write(self, username: str):
        key = self.encrypter.get_key()
        user = self.userService.find_by_username(username)
        User.key = key
        self.userService.update(user)

    def key_load(self, username: str, email: str):
        """ Loads a key from database

        :param email:
        :param str username: username
        :return: key
        :rtype: str """
        key = self.userService.find_by_username(username)
        if key is None:
            user = self.__create_user(username, email)
            return user.key
        return key

    def encrypt_data(self, username: str, data: any, email: str) -> bytes:
        """ Encrypt data and return encrypted data

        :param email:
        :param str username: username
        :param str data: data to encrypt
        :return: encrypt data
        :rtype: str"""
        key = self.key_load(username, email)
        return self.encrypter.encrypt(key, data)

    def decrypt_data(self, username: str, data_encrypted: bytes, email: str) -> bytes:
        key = self.key_load(username, email)
        return self.encrypter.decrypt(key, data_encrypted)

    def __create_user(self, username: str, email: str):
        key_encrypt = ''
        user = User(user_name=username, email=email, key=key_encrypt)
        self.userService.create(user)
        self.key_write(username)
        return user
    