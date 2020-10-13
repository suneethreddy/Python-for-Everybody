import socket

url = input('Enter a proper url: ')
port = 80
host = url.split('/')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url[2], port))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
