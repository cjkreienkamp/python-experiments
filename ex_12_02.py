import socket
import re

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

count = 0
while True:
    data = mysock.recv(3000)
    count += len(data)
    if len(data) < 1:
        break
    if count <= 3000:
        print(data.decode(),end='')

mysock.close()
print(count)
