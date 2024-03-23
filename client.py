import socket
import threading

def client_program():
    host = socket.gethostname()  
    port = 50000  # socket server port number

    client_socket = socket.socket()  

    client_socket.connect((host, port))  # connect to the server

    def receive_messages():
        while True:
            try:
                data = client_socket.recv(1024).decode()  # receive acknowledgment message
                print('Received from server: ' + data)  # show acknowledgment message
            except KeyboardInterrupt:
                break

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    try:
        while True:
            message = input("")  # take input
            client_socket.send(message.encode())  # send message
    except KeyboardInterrupt:
        pass

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
