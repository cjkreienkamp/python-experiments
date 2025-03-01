fname = input('Enter a file name: ')
if fname == 'na na boo boo':
    print('Na NA BOO BOO TO YOU - You have been punk\'d!')
    quit()
try: file = open(fname)
except: 
    print('File cannot be opened:',fname)
    quit()
count = 0
for line in file:
    if line.startswith('Subject:') == 0: continue    
    count = count+1
print('There were',count,'subject lines in',fname)
