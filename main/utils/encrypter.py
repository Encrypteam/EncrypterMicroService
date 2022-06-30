from cryptography.fernet import Fernet


class Encrypter:
    def get_key(self):
        return Fernet.generate_key()
    
    def encrypt(self, data, key) -> bytes:
        print('KEY', key)
        return Fernet(key).encrypt(data)
    
    def decrypt(self, key, data) -> bytes:
        return Fernet(key).decrypt(data)

