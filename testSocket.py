import socket


"""
addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
addr = addr_info[0][-1]

print(addr)

s = socket.socket()
s.connect(addr)

while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')

#addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

"""

"""

while True:
    pass
"""

def http_get(url):
    """
    https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html
    """
    if len(url.split('/', 3)) == 3:
        _, _, host = url.split('/', 3)
        path = ""
    else:
        _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            #todo NEVIM PROC V TOM PRIKLADU BYLO UTF8
            #print(str(data, 'utf8'), end='')
            print(str(data))
        else:
            break
    s.close()



#http_get('http://micropython.org/ks/test.html')
#http_get('http://www.translatorium.cz')

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        
    </body>
</html>
"""
#<table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:

    cl, addr = s.accept()

    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    print("Ahoj")
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
#    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
#    response = html % '\n'.join(rows)
    response = html
    #cl.send(response)
    cl.send("test")
    cl.close()
