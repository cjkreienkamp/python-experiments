file = input('Enter a file name: ')
try: text = open(file)
except:
    print('Invalid file name:',file)
    quit()

email = dict()
for line in text:
    if line.startswith('From ') is False: continue
    line = line.split()
    line = line[1]
    email[line] = email.get(line,0) + 1

# Sort the dictionary by value
lst = list()
for key, val in list(email.items()):
    lst.append((val,key))
lst.sort(reverse=True)
(maxNumber, maxEmail) = lst[0]
print(maxEmail, maxNumber)
