import socket
import threading

def new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024).decode()
        if not msg:
            print(addr, 'disconnected')
            break
        print(addr, '>>', msg)
        # Sending acknowledgment message back to the client
        ack_msg = msg
        server_info = f" {socket.gethostbyname(socket.gethostname())}:{addr[1]}: {msg}"
        clientsocket.send(server_info.encode())
        
        
    clientsocket.close()
    

s = socket.socket()
host = socket.gethostname()
port = 50000
print('server is listening on port', port)
s.bind((host, port))
s.listen(5)
try:
    while True:
        c, addr = s.accept()
        print("got connection from", addr)
        threading.Thread(target=new_client, args=(c, addr)).start()
except KeyboardInterrupt:
    print("Server interrupted, closing...")
    s.close()
