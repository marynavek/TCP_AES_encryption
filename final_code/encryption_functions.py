from hashlib import pbkdf2_hmac
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def user_input():
    password = input("Enter Passcode: ")
    return password

def generate_key(password):
    key_size = 32
    iterations = 4096
    salt = "NaCL"

    generated_key = pbkdf2_hmac('sha512', bytes(password, encoding='utf-8'),
                    bytes(salt, encoding='utf-8'), iterations, key_size)
    return generated_key

def read_file_not_encrypted(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data

def read_file(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
    return data

def encrypt_data(data, key):
    init_vector = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector))

    #pad the data to AES block size
    padder = padding.PKCS7(256).padder()
    padded_data = padder.update(bytes(data, encoding='utf-8')) + padder.finalize()
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return encrypted_data

def decrypt_data(encrypted_data, key):
    init_vector = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector))
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data

def write_to_file(data, file_name):
    with open(file_name, "a") as file:
        file.write(data)
        