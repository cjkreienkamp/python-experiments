fname = input('Enter a file name: ')
try: file = open(fname)
except: quit()
count = 0
sum = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:') == 0: continue
    count = count+1
    line = line.rstrip()
    startPos = line.find('0')
    number = float(line[startPos:])
    sum = sum + number    
print('Average spam confidence:',sum/count)
