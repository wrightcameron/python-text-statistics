from TextStatistics import TextStatistics

import socket
import argparse

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65442        # The port used by the server

# parser = argparse.ArgumentParser(description='Get statistics on text.')
# parser.add_argument('fileName', metavar='file', type=str, help='File name to parse')
# parser.add_argument("-t", "--times", help="Run process x number of times", type=int, default=0)
# #TODO Need flags for host and port
# args = parser.parse_args()
# fileName = args.fileName
fileName = 'etext/testfile.txt'

data = ""
with open(fileName, 'r') as file:
    data = file.read()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    s.sendall(data.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')

print('Received', str(data))
