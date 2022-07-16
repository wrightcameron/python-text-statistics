from cgi import test
import socket

from TextStatistics import TextStatistics

HOST = "127.0.0.1"
PORT = 65432

# TODO for now lets just have the file be handled by the server 
# and just send the response back to the client
# client sends nothing.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    # TODO Add host and port to this print message
    print('Server is up. Listening for connections...')
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        teststats = TextStatistics()
        teststats.run('./etext/testfile.txt')
        res = teststats.returnStatsAsJSON()
        print(f"Client object {conn}")
        conn.sendall(res.encode('utf-8'))
