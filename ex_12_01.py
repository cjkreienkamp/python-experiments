import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Input URL: ')
if url == '': url = 'http://data.pr4e.org/romeo.txt'

try: mysock.connect((url.split('/')[2], 80))
except:
    e = socket.gaierror
    print('Connection error: %s' % e)
    quit()

cmdStr = 'GET '+url+' HTTP/1.0\r\n\r\n'
cmd = cmdStr.encode()
try: mysock.send(cmd)
except:
    e = socket.error
    print('Error sending data: %s' % e)
    quit()    

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
   
mysock.close()
