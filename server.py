import socket
import argparse
import tempfile
from TextStatistics import TextStatistics

HOST = "127.0.0.1"
PORT = 65432


def run(host: str, port: int):
    # Create a TCP/IP socket.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Have OS reuse socket address if process dies right away
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the port.
        server_address = (host, port)
        print("starting up on {} port {}".format(*server_address))
        sock.bind(server_address)

        # Listen for incoming connections.
        sock.listen(1)

        while True:
            # Wait for a connection.
            conn, client_address = sock.accept()
            try:
                print("connection from", client_address)
                with tempfile.TemporaryFile() as tempFile:
                    while True:
                        msg = conn.recv(1024)
                        # If message length is less than 1024, it could be last line
                        if not msg or len(msg) < 1024:
                            if msg:
                                tempFile.write(msg)
                            # Hit end of line
                            break
                        tempFile.write(msg)
                    tempFile.seek(0)
                    # File recieved, now need to pass files to ProcessText
                    contents = tempFile.read().decode("utf-8")
                    response = processText(contents)
                    if response:
                        conn.sendall(response.encode("utf-8"))
            finally:
                # Clean up the connection.
                conn.close()
            print("Finished")


def processText(text: str):
    teststats = TextStatistics()
    teststats.collectStatistics(text)
    res = teststats.returnStatsAsJSON()
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ProcessTextClient: Get test statistics from server"
    )
    parser.add_argument(
        "-s", "--host", type=str, help="Server host/ip to connect too", default=HOST
    )
    parser.add_argument("-p", "--port", type=int, help="Port number", default=PORT)
    args = parser.parse_args()

    run(args.host, args.port)
