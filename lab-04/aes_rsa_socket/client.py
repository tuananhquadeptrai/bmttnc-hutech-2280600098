from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib


clinet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clinet_socket.connect(('localhost', 12345))


clinet_key = RSA.generate(2048)


sever_public_key = RSA.import_key(clinet_socket.recv(2048))
clinet_socket.send(clinet_key.publickey().export_key(format='PEM'))
encrypted_aes_key = clinet_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(clinet_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)

    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    
    return cipher.iv + ciphertext
def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()

def receive_messages():
    while True:
        encrypted_message = clinet_socket.recv(1024)
        decrypt_message = decrypt_message(aes_key, encrypted_message)
        print(f"Received message: {decrypt_message}")
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

while True:
    message= input("Enter message to send ('exit' to quit): ")
    encrypted_message = encrypt_message(aes_key, message)
    clinet_socket.send(encrypted_message)
    if message == "exit":
        break
clinet_socket.close()