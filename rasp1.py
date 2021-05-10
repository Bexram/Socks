import socket

ip_server='127.0.0.1'
sock = socket.socket()
sock.connect((ip_server, 8080))
stri = 'hello, world!'
sock.send(stri.encode())
sock.close()
