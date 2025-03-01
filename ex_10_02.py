file = input('Enter a file name: ')
try: text = open(file)
except:
    print('Invalid file name:',file)
    quit()

hour = dict()
for line in text:
    if line.startswith('From ') is False: continue
    line = line.split()
    line = line[5]
    line = line.split(':')
    hour[line[0]] = hour.get(line[0],0) + 1

t = list()
for key, val in hour.items():
    t.append((key,val))
t.sort(reverse = False)
for key, val in t:
    print(key,val)
