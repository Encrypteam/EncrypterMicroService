from main.utils import Encrypter


class EncrypterService:
    def __init__(self):
        self.encrypter = Encrypter()

    def key_write(self, username: str):
        key = self.encrypter.get_key()

    def key_load(self, username: str, email: str):
        """ Loads a key from database

        :param str username: username
        :return: key
        :rtype: str """
        pass

    def encrypt_data(self, username: str, data: any, email: str) -> bytes:
        """ Encrypt data and return encrypted data

        :param str username: username
        :param str data: data to encrypt
        :return: encrypt data
        :rtype: str"""
        key = self.key_load(username, email)
        return self.encrypter.encrypt(data, key)

    def decrypt_data(self, username: str, data_encrypted: bytes, email: str) -> bytes:
        key = self.key_load(username, email)
        return self.encrypter.decrypt(key, data_encrypted)

    