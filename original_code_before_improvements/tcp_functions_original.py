import socket
from sys import getsizeof
import os

from encrypt_decrypt_functions import decrypt_data, read_file, write_to_file

def client(encrypted_data_file, new_file_name, port=None):
    IP = socket.gethostbyname(socket.gethostname())
    if port is not None:
        PORT = port
    else:
        PORT = 4455
    ADDR = (IP, PORT)
    FORMAT = "utf-8"
    SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    file = open(encrypted_data_file, "rb")
    data = file.read()
    data_size = getsizeof(data)

    """ Sending file name and size. """
    client.send(f"{new_file_name}{SEPARATOR}{data_size}".encode())

    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Sending the file data to the server. """

    with open(encrypted_data_file, "rb") as f:
        while True:
            bytes_read = f.read(SIZE)
            if not bytes_read:
                break
            client.sendall(bytes_read)

    """ Closing the connection from the server. """
    client.close()


def server(key, selected_file_name=None, port=None):
    IP = socket.gethostbyname(socket.gethostname())
    if port is not None:
        PORT = port
    else:
        PORT = 4455
    ADDR = (IP, PORT)
    SIZE = 4096
    FORMAT = "utf-8"
    SEPARATOR = "<SEPARATOR>"

    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    server.listen()
    print("[LISTENING] Server is listening.")

    while True:

        client_socket, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")

        received = client_socket.recv(SIZE).decode()
        print(f"[NEW CONNECTION] {addr} connected.")
        client_socket.send("Filename received.".encode(FORMAT))
        # print(received)
        filename, filesize = received.split(SEPARATOR)
        # remove absolute path if there is
        filename = os.path.basename(filename)
        # convert to integer
        # print(filesize)
        filesize = int(filesize)
        

        if selected_file_name is not None:
            filename = selected_file_name

        # rcvd_data = ""
        with open("encrypted_data_2.txt", "wb") as f:
            while True:
                bytes_read = client_socket.recv(SIZE)
                if not bytes_read:
                    break
                # rcvd_data = rcvd_data + bytes_read
                f.write(bytes_read)
        
        encrypted_data = read_file("encrypted_data.txt")
        decrypted_data = decrypt_data(encrypted_data, key)
        write_to_file(decrypted_data.decode("utf-8", errors='ignore'), filename)

        
        client_socket.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
