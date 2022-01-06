import socket
import argparse
import sys

sys.path.append('..')
from TextStatistics import TextStatistics

HOST = '127.0.0.1'
PORT = 65442

parser = argparse.ArgumentParser(description='Launch text statistics server.')
parser.add_argument('-s', '--server', type=str, default=HOST,help='Server ip or host to launch server on, default is {}'.format(HOST))
parser.add_argument('-p', '--port', type=str, default=PORT, help='Port to launch server on, default is {}'.format(PORT))
args = parser.parse_args()
host = args.server
port = args.port


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Send text to Text Statistics
            w = TextStatistics()
            w.collectStatistics(str(data))
            conn.sendall(str(w).encode('utf-8'))
