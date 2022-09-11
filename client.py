import socket
import os
import argparse

HOST = "127.0.0.1"
PORT = 65432


def run(host: str, port: int, fileName: str):
    # Check if file exists
    if not os.path.isfile(fileName):
        print(f"File {fileName} doesn't exist. Exiting...")
        exit(1)

    # Use with statement New
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.settimeout(5)
        # Send text file to server
        print(f"Sending file {fileName}")
        file = open(fileName, "rb")
        # TODO What if the file is empty?
        buf = file.read(1024)
        while (buf):
            sock.send(buf)
            buf = file.read(1024)
        print("Finished sending file to host")
        # Look for the response.
        msg = sock.recv(1024).decode('utf-8')
        # TODO Format Text, its being returned as json
        print(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ProcessTextClient: Get test statistics from server')
    parser.add_argument('-s', '--host', type=str, help='Server host/ip to connect too', default=HOST)
    parser.add_argument('-p', '--port', type=int, help='Port number', default=PORT)
    # TODO Add way to pass nargs, will need to put run into loop
    parser.add_argument('fileName', metavar='file', type=str, help='File name to parse')
    args = parser.parse_args()

    run(args.host, args.port, args.fileName)
