fname = input('Enter a file name: ')
try: file = open(fname)
except: quit()
for line in file:
    noJumpLine = line.rstrip()
    uppLine = noJumpLine.upper()
    print(uppLine)
