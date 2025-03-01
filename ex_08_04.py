file = input('Enter file: ')
try: text = open(file)
except: quit()
t = list()
for line in text:
    line = line.split()
    for word in line:
        if word in t: continue
        t.append(word)
t.sort()
print(t)
