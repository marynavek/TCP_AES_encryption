from Crypto.Cipher import AES
from hashlib import pbkdf2_hmac
from Crypto.Util.Padding import pad, unpad


def user_input():
    password = input("Enter Passcode: ")
    return password


def generate_password(password):
    key_size = 32
    iterations = 4096
    salt = "NaCL"
    dk = pbkdf2_hmac('sha512', bytes(password, encoding='utf-8'), bytes(salt, encoding='utf-8'), iterations, key_size)
    return dk

def read_file_not_encrypted(file_path):
    f = open(file_path, "r")
    return f.read()


def read_file(file_path):
    f = open(file_path, "rb")
    return f.read()

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)

    encrypted_data = cipher.encrypt(pad(bytes(data, encoding='utf-8'), AES.block_size))
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data

def write_to_file(data, file_name):
    f = open(file_name, "a")
    f.write(data)
    f.close()
