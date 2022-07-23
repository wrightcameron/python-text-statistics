from cgi import test
import socket

from TextStatistics import TextStatistics

HOST = "127.0.0.1"
PORT = 65432

# TODO for now lets just have the file be handled by the server 
# and just send the response back to the client
# client sends nothing.

def processText(text: str):
    teststats = TextStatistics()
    teststats.collectStatistics(text)
    res = teststats.returnStatsAsJSON()
    return res

def run(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        # TODO This time out is not needed
        #s.settimeout(10)
        s.listen()
        # TODO Add host and port to this print message
        print('Server is up. Listening for connections...')
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            # Get all text sent from client
            text = ""
            while True:
                msg = conn.recv(1024)
                # If message length is less than 1024, it could be last line
                if not msg or len(msg) < 1024:
                    if msg:
                        text += msg.decode('utf-8')
                    # Hit end of line
                    break
                text += msg.decode('utf-8')
            res = processText(text)
            print(f"Client object {conn}")
            conn.sendall(res.encode('utf-8'))
            # TODO Need to exit gracefully tell server we don't need the port

run(HOST, PORT)
# TODO Uncomment when closer to completion
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='ProcessTextClient: Get test statistics from server')
#     parser.add_argument('-h', '--host', type=str, help='Server host/ip to connect too', default=HOST)
#     parser.add_argument('-p', '--port', type=int, help='Port number', default=PORT)
#     args = parser.parse_args()

#     run(args.host, args.port)
