import argparse

from encryption_functions import encrypt_data, generate_key, read_file_not_encrypted, user_input
from tcp_functions import client_connection

# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument("--input_file_path", type=str, required=True, help = "input_file")
parser.add_argument("--local_encryption", type=str, required=True,
                        help='local encryption or via TCP connection')
parser.add_argument("--port", type=int, required=False,
                    help='tcp port if sending via TCP connection')

if __name__ == "__main__":
    args = parser.parse_args()
    file_path = args.input_file_path
    local_encryption = args.local_encryption
    port = args.port
    password = user_input()

    key = generate_key(password)

    file_data = read_file_not_encrypted(file_path)

    encrypted_data = encrypt_data(file_data, key)


    ENCRYPTED_DATA_FILE = "encrypted_data.txt"

    with open(ENCRYPTED_DATA_FILE, "wb") as file:
        file.write(encrypted_data)

    if local_encryption == "False":
        client_connection(ENCRYPTED_DATA_FILE, "decrypted_data.txt")
