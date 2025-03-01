email = dict()
file = input('Enter file name: ')
try: text = open(file)
except:
    ('File name invalid:',file)
    quit()

for line in text:
    if line.startswith('From ') is False: continue
    line = line.split()
    word = line[1]
    email[word] = email.get(word,0) + 1
mostMail =  None
for address in email:
    if mostMail is None: mostMail = address
    if email[address] > email[mostMail] :
        mostMail = address
print(mostMail,email[mostMail])
