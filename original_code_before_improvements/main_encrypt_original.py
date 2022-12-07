import argparse

from encrypt_decrypt_functions import encrypt_data, generate_password, read_file, read_file_not_encrypted, user_input
from tcp_functions import client_connection


# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument("--input_file_path", type=str, required=True, help = "input_file")
parser.add_argument("--local_encryption", type=str, required=True, help='local encryption or via TCP connection')
parser.add_argument("--port", type=int, required=False, help='tcp port if sending via TCP connection')

if __name__ == "__main__":
    args = parser.parse_args()
    file_path = args.input_file_path
    local_encryption = args.local_encryption
    port = args.port
    
    password = user_input()

    key = generate_password(password)

    file_data = read_file_not_encrypted(file_path)

    encrypted_data = encrypt_data(file_data, key)


    encrypted_data_file = "encrypted_data.txt"

    with open(encrypted_data_file, "wb") as file:
        file.write(encrypted_data)

    if local_encryption == "False":
        client_connection(encrypted_data_file, "decrypted_data.txt")
