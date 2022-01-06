import socket
import argparse
import sys

sys.path.append('..')
from TextStatistics import TextStatistics

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65442        # The port used by the server

parser = argparse.ArgumentParser(description='Launch text statistics server.')
parser.add_argument('fileName', metavar='file', type=str, help='File name to parse')
parser.add_argument('-s', '--server', type=str, default=HOST,help='Server ip or host to launch server on, default is {}'.format(HOST))
parser.add_argument('-p', '--port', type=str, default=PORT, help='Port to launch server on, default is {}'.format(PORT))
args = parser.parse_args()
host = args.server
port = args.port
fileName = args.fileName

data = ""
with open(fileName, 'r') as file:
    data = file.read()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    s.sendall(data.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')

print('Received', str(data))
