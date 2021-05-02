import socket
HOST = 'localhost'
PORT = 8090

requests = ['GET /pwd/', 'GET /ls/', 'GET /mkdir/new', 'GET /rmdir/new', 'GET /delete/picture.png', 'GET /rename/index.html/index.html', 'GET /receive/index.html', 'GET /stop/']
sock = socket.socket()
try:
    sock.connect((HOST, PORT))
except Exception as e:
    print(e)
for request in requests:
    sock.send(request.encode())
    try:
        response = sock.recv(1024).decode()
    except Exception as e:
        print(request)
        print(e)
    if response == 'error':
        print('Error in ' + request)
sock.close()