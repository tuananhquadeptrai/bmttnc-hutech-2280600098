import ecdsa
import os

KEYS_DIR = 'cipher/ecc/keys'
if not os.path.exists(KEYS_DIR):
    os.makedirs(KEYS_DIR)

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()        # Tạo khóa riêng tư
        vk = sk.get_verifying_key()             # Lấy khóa công khai từ khóa riêng
        with open(f'{KEYS_DIR}/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
        with open(f'{KEYS_DIR}/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open(f'{KEYS_DIR}/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        with open(f'{KEYS_DIR}/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        return sk, vk

    def sign(self, message, key):
        # message là str, phải encode về bytes
        return key.sign(message.encode('ascii'))

    def verify(self, signature, message, key=None):
        # key là VerifyingKey (khóa công khai). Nếu không truyền vào thì tự load.
        if key is None:
            _, vk = self.load_keys()
        else:
            vk = key
        if isinstance(message, str):
            message_bytes = message.encode('ascii')
        else:
            message_bytes = message
        try:
            return vk.verify(signature, message_bytes)
        except ecdsa.BadSignatureError:
            return False
