domainName = dict()
file = input('Enter a file name: ')
try: text = open(file)
except:
    print('File name invalid:',file)
    quit()

for line in text:
    if line.startswith('From ') is False: continue
    line = line.split()
    line = line[1].split('@')
    word = line[1]
    domainName[word] = domainName.get(word,0) + 1
print(domainName)
