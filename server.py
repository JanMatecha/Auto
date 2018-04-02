# Socket server in python using select function

import socket
import select
import time
import sys

from motor import Motor
motor=Motor()
motor.forward()
motor.backward()


from oled import *

oled = Oled()
oled.head()
oled.square()
oled.foot("START")



CONNECTION_LIST = []  # list of socket clients
RECV_BUFFER = 1024  #4096  # Advisable to keep it as an exponent of 2
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this has no effect, why ?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)

# Add server socket to the list of readable connections
CONNECTION_LIST.append(server_socket)

print("Chat server started on port " + str(PORT))
oled.foot("PORT: " + str(PORT))
a=1
while 1:
    # Get the list sockets which are ready to be read through select
    read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])
    #time.sleep(1)
    #print(a)
    #a+=1
    #print(read_sockets, write_sockets, error_sockets)

    for sock in read_sockets:

        # New connection
        if sock == server_socket:
            # Handle the case in which there is a new connection recieved through server_socket
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
            print("Client (%s, %s) connected" % addr)
            oled.foot("%s" % addr[0])

        # Some incoming message from a client
        else:
            # Data recieved from client, process it
            try:
                # In Windows, sometimes when a TCP program closes abruptly,
                # a "Connection reset by peer" exception will be thrown
                data = sock.recv(RECV_BUFFER)




                # echo back the client message
                if data:
                    print("data: ", data.decode('utf-8'))
                    reply = 'OK...' + data.decode('utf-8')
                    oled.foot(data.decode('utf-8'))
                    print('server: ', addr, reply)
                    sock.send(reply.encode('utf-8'))
                    prikaz, parametr = data.decode('utf-8').split(":")
                    if data.decode('utf-8') == "konec":
                        print("prikaz: konec")
                        oled.foot("prikaz: konec")
                        server_socket.close()
                        #TODO porad to nefunguje
                        sys.exit()
                    duration = 0.5
                    if prikaz == "MF":
                        motor.forward(velocity=int(parametr), duration=duration)
                    if prikaz == "MB":
                        motor.backward(velocity=int(parametr), duration=duration)

            # client disconnected, so remove from socket list
            except:
                #TODO nevim co to melo delat
                # broadcast_data(sock, "Client (%s, %s) is offline" % addr)

                print("Client (%s, %s) is offline" % addr)
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue

server_socket.close()


