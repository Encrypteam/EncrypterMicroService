import unittest

from main import create_app, db
from main.services import EncrypterService


class TestEncrypterService(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.encrypterService = EncrypterService()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_encrypt_data(self):
        username = 'test'
        data = 'sadhfbsadhfbsaldfbfsdf'.encode()
        email = 'test@example.com'
        data_encrypted = self.encrypterService.encrypt_data(username, data, email)
        self.assertIsNotNone(data_encrypted)

    def test_decrypt_data(self):
        username = 'test2'
        data = 'sadhfbsadhfbsaldfbfsdf'
        email = 'test2@example.com'
        data_encrypted = self.encrypterService.encrypt_data(username, data.encode(), email)
        data_decrypted = self.encrypterService.decrypt_data(username, data_encrypted, email)
        self.assertEqual(data, data_decrypted.decode())