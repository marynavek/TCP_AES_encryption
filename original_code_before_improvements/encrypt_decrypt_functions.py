from hashlib import pbkdf2_hmac
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def user_input():
    password = input("Enter Passcode: ")
    return password

def generate_password(password):
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
    cipher = AES.new(key, AES.MODE_CBC)

    encrypted_data = cipher.encrypt(pad(bytes(data, encoding='utf-8'), AES.block_size))
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data

def write_to_file(data, file_name):
    with open(file_name, "a") as file:
        file.write(data)
        