'''
    Simple udp socket server
'''

import socket
import sys

print("ZACATEK")
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break

    reply = 'OK...'.encode('utf-8') + data
    print(reply.decode('ascii'))
#    s.sendto(reply, addr)
    s.sendto(data, addr)
    print('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.decode('ascii').strip())
    if data.decode('ascii') == "konec":
        print("uz je konec")
        break
    else:
        print("jeste neni  konec")

s.close()
