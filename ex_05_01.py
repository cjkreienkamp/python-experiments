sum = 0
i = 0
num = 0
while num != 'done' :
    num = input('Enter a number: ')
    try:
        num = float(num)
    except:
        print('Invalid input')
        continue
    i = i+1
    sum = sum + num
average = sum/i
print(sum, i, average)
