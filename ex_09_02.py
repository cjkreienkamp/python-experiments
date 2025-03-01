weekday = dict()
file = input('Enter a file name: ')
try: text = open(file)
except:
    print('File name invalid:',file)
    quit()

for line in text:
    if line.startswith('From ') is False: continue
    words = line.split()
    word = words[2]
    weekday[word]  = weekday.get(word,0) + 1
print(weekday)  
