import socket
import argparse
import os

HOST = "127.0.0.1"
PORT = 65432

def run(host: str, port: int, fileName: str):
    # Check if file exists
    if not os.path.isfile(fileName):
        print(f"File {fileName} doesn't exist. Exiting...")
        exit(1)
    # Open file and store it in variable
    with open(fileName) as f:
        text = f.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((host, port))
        # Send text file to server
        s.sendall(text.encode('utf-8'))
        while True:
            # TODO Send to the server the file path to the file it will analyze
            msg = s.recv(1024)

            if not msg:
                print('No messages from the server. Closing the connection...')
                break

            print(f"Message from server: { msg.decode('utf-8') }")
            print(f"Type of recieved message: {type(msg)}")

run(HOST, PORT, './etext/testfile.txt')
# TODO Uncomment when closer to completion
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='ProcessTextClient: Get test statistics from server')
#     parser.add_argument('-h', '--host', type=str, help='Server host/ip to connect too', default=HOST)
#     parser.add_argument('-p', '--port', type=int, help='Port number', default=PORT)
#     parser.add_argument('fileName', metavar='file', type=str, nargs='+', help='File name to parse')
#     args = parser.parse_args()

#     run(args.host, args.port, args.fileName)
