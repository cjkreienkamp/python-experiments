file = input('Enter a file name: ')
try: text = open(file)
except: quit()
count = 0
for line in text:
    if line.startswith('From ') is False : continue
    count = count + 1
    line = line.split()
    print(line[1])
print('There were %d lines in the file with From as the first word' % count)
