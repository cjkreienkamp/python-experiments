t = list()
while(True):
    num = input('Enter a number: ')
    if num == 'done': break
    try: num = float(num)
    except:
        print('Invalid input')
        continue
    t.append(num)
print('Maximum:',max(t))
print('Minimum:',min(t))
