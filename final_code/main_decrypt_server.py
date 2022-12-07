import argparse

from encryption_functions import decrypt_data, generate_key, read_file, user_input, write_to_file
from tcp_functions import server_connection


# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument("--local_encryption", type=str, required=True,
                    help='local encryption or via TCP connection')
parser.add_argument("--input_file_path", type=str, required=False, help = "input_file")
parser.add_argument("--port", type=int, required=False,
                help='tcp port if sending via TCP connection')

if __name__ == "__main__":
    args = parser.parse_args()
    local_encryption = args.local_encryption
    file_path = args.input_file_path
    port = args.port
    password = user_input()

    key = generate_key(password)

    DECRYPTED_DATA_FILENAME = "decrypted_data.txt"

    if local_encryption == "True":
        encrypted_data = read_file(file_path)
        print(type(encrypted_data))
        decrypted_data = decrypt_data(encrypted_data, key)
        write_to_file(decrypted_data.decode("utf-8", errors='ignore'), DECRYPTED_DATA_FILENAME)
    else:
        server_connection(key)
