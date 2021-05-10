import socket


def initServer():
    sock = socket.socket()
    sock.bind(('', 8081))
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
        print('From Server: ' + data)
        if data:
            print('Action')
        else:
            print('Nothing data. Close conn')
            break
    conn.close()


s=initServer()
while True:
    dataTransfer(initConn())