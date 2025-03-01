import re
file = input('Enter file: ')
try: fhand = open(file)
except: 
    print('Invalid file name:',file)
    quit()

sum = 0
number = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]*)',line)
    if len(x)>0: 
        number +=1
        sum += int(x[0])
print(int(sum/number))
