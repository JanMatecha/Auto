'''
https://www.binarytides.com/python-socket-programming-tutorial/
prvni priklad
'''

import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
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


# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    # display client information
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(1024)
    reply = 'OK...' + data.decode('utf-8')
    print(reply)

    if not data:
        break

    conn.sendall(reply.encode('utf-8'))

conn.close()
s.close()

