import re

regEx = input('Enter a regular expression: ')
file = open('mbox.txt')

count = 0
for line in file:
    line = line.rstrip()
    if re.search(regEx,line): count += 1
print('mbox.txt had',count,'lines that matched',regEx)
