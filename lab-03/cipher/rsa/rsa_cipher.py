import rsa
import os

# Đảm bảo thư mục keys tồn tại
KEYS_DIR = 'cipher/rsa/keys'
if not os.path.exists(KEYS_DIR):
    os.makedirs(KEYS_DIR)

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open(f'{KEYS_DIR}/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open(f'{KEYS_DIR}/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open(f'{KEYS_DIR}/publicKey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open(f'{KEYS_DIR}/privateKey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key, public_key

    def encrypt(self, message, key):
        # message phải là chuỗi, key là public_key hoặc private_key
        return rsa.encrypt(message.encode('ascii'), key)

    def decrypt(self, ciphertext, key):
        # ciphertext là bytes, key là private_key hoặc public_key
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except Exception:
            return ''

    def sign(self, message, key):
        # message là chuỗi, private_key là private_key object
        return rsa.sign(message.encode('ascii'), key, 'SHA-1')

    def verify(self, message, signature, key):
        # message là chuỗi, signature là bytes, public_key là public_key object
        try:
            rsa.verify(message.encode('ascii'), signature, key)
            return True
        except :
            return False
