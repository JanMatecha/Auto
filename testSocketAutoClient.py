import socket  # for sockets
import sys  # for exit

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()

print('Socket Created')

host = '127.0.0.1'
#host = '10.0.0.10'
port = 8888


# Connect to remote server
s.connect((host, port))


print('Socket Connected to ' + host )

# Send some data to remote server

for cislo in range(1):
    message = "Zprava" + str( cislo)
    message = "konec"
    message = "MF:50"
    message = "MB:50"


    try:
        # Set the whole string
        s.sendall(message.encode('utf-8'))
    except socket.error:
        # Send failed
        print('Send failed')
        sys.exit()

    print('Message send successfully')

    # Now receive data
    reply = s.recv(4096)

    print(reply.decode('ascii'))

s.close()
