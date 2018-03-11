'''
udp socket client
'''

import socket   #for sockets
import sys  #for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

#host = 'localhost'
host = '10.0.0.6'
port = 8888

while 1:
    msg = input('Enter message to send : ')

    try:
        #Set the whole string
        print(type(msg.encode('utf-8')))
        s.sendto(msg.encode('utf-8'), (host, port))

        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print('Server reply : ' + reply.decode('ascii'))

    except socket.error as msg:
        print
        print("Socket Error: %s" % msg)
        sys.exit()
