import urllib.request

url = input('Enter URL: ')
if url == '': url = 'http://data.pr4e.org/romeo.txt'
try: fhand = urllib.request.urlopen(url)
except:
    print('Invalid URL')
    quit()

length = 0
for line in fhand:
    prevlength = length
    length += len(line.decode())
    if length <= 3000:
        print(line.decode().strip())
    elif prevlength < 3000:
        print(line.decode().strip()[:3000-prevlength])
print(length)
