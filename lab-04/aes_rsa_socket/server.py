from Crypto.Cipher import AES ,PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib



sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.bind(('localhost', 12345))
sever_socket.listen(5)
server_key = RSA.generate(2048)
clients =[]


def encrypt_message(key , message):
    cipher = AES.new(key, AES.MODE_CBC)
    
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext


def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypt_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypt_message.decode()


def handle_client(client_socket, client_address):
    print(f" Connected with {client_address}")
    
    # Send public key to client
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    
    # Receive AES key from client
    client_received_key = RSA.import_key(client_socket.recv(2048))
    
    aes_key = get_random_bytes(16)  
    cipher_rsa = PKCS1_OAEP.new(client_received_key)    
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)
    
    clients.append((client_socket,aes_key))
    
    while True:
        encrypted_message = client_socket.recv(1024)
        decrypted_message = decrypt_message(aes_key, encrypted_message)
        print(f"Received message from {client_address}: {decrypted_message}")
        
        
        for clinet , key in clients:
            if clinet != client_socket:
                encrypted = encrypt_message(key,decrypted_message)
                clinet.send(encrypted)
        if decrypted_message == "exit":
            break
    clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Connection with {client_address} closed.")
while True:
    client_socket, client_address = sever_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
    
                