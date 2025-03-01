file = input('Enter a file name: ')
try: text = open(file)
except: quit()
dictionary = dict()
for line in text:
    line = line.split()
    for word in line:
        dictionary[word] = ' '
while(True):
    check = input('Enter a word: ')
    if check == 'done': quit()
    if check in dictionary: print(check,'is in the file')
    else: print(check, 'is not in the file')
