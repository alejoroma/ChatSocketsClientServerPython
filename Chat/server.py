import socket
from _thread import *

s_socket = socket.socket()
host_name = '127.0.0.1'
port = 8001
threadCount = 0
try:
    s_socket.bind((host_name, port))
except socket.error as e:
    print(str(e))
    
print("Servidor en espera ...")
s_socket.listen(5)
buffer_size = 1024

def multi_threaded_client(connection):
    while True:
        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        recv_data = connection.recv(1024).decode()
        if not recv_data:
            # if data is not received break
            break
       
        print("USER: " + str(address[1]) + ": "+ str(recv_data))
        print(str(address[1]))
        recv_data = input(' -> ')
        connection.send(recv_data.encode())  # send data to the client

    connection.close()


while True:
    Client, address = s_socket.accept()
    print('Conectado a: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    threadCount +=1
    print('Conexiones: ' + str(threadCount))
s_socket.close()