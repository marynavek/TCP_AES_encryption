import socket
from sys import getsizeof
import os

from encryption_functions import decrypt_data, read_file, write_to_file


def client_connection(encrypted_data_file, new_file_name, port=None):
    IP = socket.gethostbyname('localhost')
    if port is None:
        port = 4455
    addr = (IP, port)
    size = 4096
    separator = "<SEPARATOR>"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(addr)

    with open(encrypted_data_file, "rb") as file:
        data = file.read()
        data_size = getsizeof(data)

    client.send(f"{new_file_name}{separator}{data_size}".encode())

    msg = client.recv(size).decode("utf-8")
    print(f"[SERVER]: {msg}")

    with open(encrypted_data_file, "rb") as file:
        while True:
            bytes_read = file.read(size)
            if not bytes_read:
                break
            client.sendall(bytes_read)

    client.close()


def server_connection(key, selected_file_name=None, port=None):
    IP = socket.gethostbyname('localhost')
    if port is None:
        port = 4455
    addr = (IP, port)
    size = 4096
    separator = "<SEPARATOR>"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(addr)

    server.listen()
    print("[LISTENING] Server is listening.")

    while True:

        client_socket, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        received = client_socket.recv(size).decode()
        print(f"[NEW CONNECTION] {addr} connected.")
        client_socket.send("Filename received.".encode("utf-8"))
        filename, filesize = received.split(separator)
        filename = os.path.basename(filename)
        filesize = int(filesize)

        if selected_file_name is not None:
            filename = selected_file_name

        with open("encrypted_data_2.txt", "wb") as file:
            while True:
                bytes_read = client_socket.recv(size)
                if not bytes_read:
                    break
                file.write(bytes_read)
        encrypted_data = read_file("encrypted_data.txt")
        decrypted_data = decrypt_data(encrypted_data, key)
        write_to_file(decrypted_data.decode("utf-8", errors='ignore'), filename)

        client_socket.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
