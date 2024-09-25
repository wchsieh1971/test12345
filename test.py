import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        client_socket, client_address = server_socket.accept()

        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            data = b''
            while True:
                chunk = client_socket.recv(16)
                if chunk:
                    data += chunk
                else:
                    break
            text = data.decode('utf-8')
            print('received {!r}'.format(text))
            print('sending data back to the client')
            client_socket.sendall(data)

        finally:
            # Clean up the connection
            client_socket.close()

start_server()