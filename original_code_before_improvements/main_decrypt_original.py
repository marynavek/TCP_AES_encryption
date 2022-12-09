import argparse

from encrypt_decrypt_original import decrypt_data, encrypt_data, generate_password, read_file, user_input, write_to_file
from tcp_functions_original import server


# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument("--local_encryption", type=str, required=True, help='local encryption or via TCP connection')
parser.add_argument("--input_file_path", type=str, required=False, help = "input_file")
parser.add_argument("--port", type=int, required=False, help='tcp port if sending via TCP connection')

if __name__ == "__main__":
    # main()
    args = parser.parse_args()
    local_encryption = args.local_encryption
    file_path = args.input_file_path
    port = args.port
    
    password = user_input()

    key = generate_password(password)

    decrypted_data_file_name = "decrypted_data.txt"

    if local_encryption == "True":
        encrypted_data = read_file(file_path)
        print(type(encrypted_data))
        decrypted_data = decrypt_data(encrypted_data, key)
        write_to_file(decrypted_data.decode("utf-8", errors='ignore'), decrypted_data_file_name)
    else:
        server(key)