import unittest
from main.utils.encrypter import Encrypter


class TestEncrypter(unittest.TestCase):

    def test_get_key(self):
        encrypter = Encrypter()
        key = encrypter.get_key()
        self.assertIsNotNone(key)

    def test_encrypt_decrypt_data(self):
        encrypter = Encrypter()
        key = encrypter.get_key()
        data = 'test'
        encrypted_data = encrypter.encrypt(key, data.encode())
        self.assertIsNotNone(encrypted_data)
        decrypted_data = encrypter.decrypt(key, encrypted_data).decode()
        self.assertEqual(data, decrypted_data)

