import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Input URL: ')
if url == '': url = 'http://data.pr4e.org/romeo.txt'

try:
    mysock.connect((url.split('/')[2], 80))
    cmdStr = 'GET '+url+' HTTP/1.0\r\n\r\n'
    cmd = cmdStr.encode()
    mysock.send(cmd)
except:
    print('Please enter a valid url')
    quit()

dontprint = True
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    if dontprint == False: print(data.decode(),end='')
    else:
        start = data.decode().find('\r\n\r\n')
        print(data.decode()[start+4:],end='')
        dontprint = False

mysock.close()
