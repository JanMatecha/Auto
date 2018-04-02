
import socket
import sys
from _thread import *

HOST = '127.0.0.1'
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket now listening')


# Function for handling connections. This will be used to create threads
def client_thread(conn, addr):
    # Sending message to connected client
    print("Server: client_thread")
    conn.send('Welcome to the server. Type something and hit enter\n'.encode('utf-8'))  # send only takes string

    # infinite loop so that function do not terminate and thread do not end.
    while True:

        # Receiving from client
        try:
            data = conn.recv(1024)
            #data = "TEST".encode('utf-8')
            reply = 'OK...' + data.decode('utf-8')
            if not data:
                break
            print('Server: ', addr, reply)
            conn.sendall(reply.encode('utf-8'))
        except socket.error as msg:
            print("chyba: ", msg)
            break

    # came out of loop
    conn.close()


# now keep talking with the client
a=0
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    # display client information
    print('SERVER: Connected with ' + addr[0] + ':' + str(addr[1]))

    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(client_thread, (conn,addr))
    print(a)
    a += 1




s.close()

