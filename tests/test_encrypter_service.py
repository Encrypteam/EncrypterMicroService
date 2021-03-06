import unittest

from main import create_app
from main.services import EncrypterService


class TestEncrypterService(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.encrypterService = EncrypterService()

    def tearDown(self):
        self.app_context.pop()

    def test_encrypt_data(self):
        username = 'juan'
        data = 'sadhfbsadhfbsaldfbfsdf'.encode()
        email = 'juan@example.com'
        data_encrypted = self.encrypterService.encrypt_data(username, data, email)
        self.assertIsNotNone(data_encrypted)

    def test_decrypt_data(self):
        username = 'juan'
        data = 'sadhfbsadhfbsaldfbfsdf'.encode()
        email = 'juan@example.com'
        data_encrypted = self.encrypterService.encrypt_data(username, data, email)
        data_decrypted = self.encrypterService.decrypt_data(username, data_encrypted, email)
        self.assertEqual(data, data_decrypted)
