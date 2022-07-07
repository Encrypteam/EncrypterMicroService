from cryptography.fernet import Fernet


class Encrypter:
    def get_key(self):
        return Fernet.generate_key()
    
    def encrypt(self, key, data) -> bytes:
        f = Fernet(key)
        return f.encrypt(data)

    def decrypt(self, key, data) -> bytes:
        f = Fernet(key)
        return f.decrypt(data)
