def chop(t):
    del t[len(t)-1]
    del t[0]

def middle(t):    
    return t[1:-1]

t = list()
while(True):
    word = input('Input a number or letter: ')
    if word == 'done': break
    t.append(word)
print('Original List:',t)
print('Middle:',middle(t))
print('Chopped:',chop(t),'   t:',t)

