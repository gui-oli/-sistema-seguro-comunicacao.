import bcrypt
import jwt
import datetime

SECRET_KEY = "Trabalho"  # Troque por uma chave secreta mais segura

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    @staticmethod
    def generate_token(username):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode({'username': username, 'exp': expiration}, SECRET_KEY, algorithm='HS256')
        return token