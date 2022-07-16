import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    while True:
        msg = s.recv(1024)

        if not msg:
            print('No messages from the server. Closing the connection...')
            break

        print(f"Message from server: { msg.decode('utf-8') }")
        print(f"Type of recieved message: {type(msg)}")
