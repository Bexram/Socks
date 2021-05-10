import socket

ip_rasp2='127.0.0.1'


def initServer():
    sock = socket.socket()
    sock.bind(('', 8080))
    print('Server started')
    return sock

def initConn():
    s.listen(1)
    conn, addr = s.accept()
    print('connected:', addr)
    return conn

def dataTransfer(conn):
    while True:
        data = conn.recv(1024).decode()
        print('From Rasp1: ' + data)
        if data:
            sock = socket.socket()
            sock.connect((ip_rasp2, 8081))
            sock.send(data.encode())
            print('To Rasp2: '+data)
            sock.close()
        else:
            print('Nothing data. Close conn')
            break
    conn.close()


s=initServer()
while True:
    dataTransfer(initConn())