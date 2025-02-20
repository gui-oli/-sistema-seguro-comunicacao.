from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class Message:
    def __init__(self):
        self.keys = {}

    def generate_keys(self):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        public_key = private_key.public_key()
        self.keys['private'] = private_key
        self.keys['public'] = public_key
        return private_key, public_key

    def encrypt_message(self, message, recipient_public_key):
        # Gera uma chave AES
        aes_key = Fernet.generate_key()
        fernet = Fernet(aes_key)

        # Criptografa a mensagem com AES
        encrypted_message = fernet.encrypt(message.encode())

        # Criptografa a chave AES com a chave pública do destinatário
        encrypted_aes_key = recipient_public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encrypted_aes_key, encrypted_message

    def decrypt_message(self, encrypted_aes_key, encrypted_message):
        # Descriptografa a chave AES com a chave privada
        aes_key = self.keys['private'].decrypt(
            encrypted_aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Descriptografa a mensagem com AES
        fernet = Fernet(aes_key)
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        return decrypted_message