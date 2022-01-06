import socket
import argparse

from TextStatistics import TextStatistics

# parser = argparse.ArgumentParser(description='Launch text statistics server.')
# parser.add_argument('Host', metavar='host', type=str, help='Host name to launch server on')
# parser.add_argument('Port', metavar='port', type=str, help='Port to launch server on')

HOST = '127.0.0.1'
PORT = 65442

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
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
