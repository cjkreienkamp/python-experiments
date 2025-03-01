import string

file = input('Enter a file name: ')
try: text = open(file)
except:
    print('Invalid file name:',file)
    quit()

letters = dict()
for line in text:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.translate(str.maketrans('','',string.digits))
    line = line.lower().strip().replace(' ','').replace('\t','')
    for char in line:
        letters[char] = letters.get(char,0) + 1
t = sorted([ (val,key) for key,val in letters.items()], reverse = True)
# t = list()
# for key, val in letters.items():
#     t.append((val,key))
# t.sort(reverse = True)
for val, key in t:
     print(key, val)
