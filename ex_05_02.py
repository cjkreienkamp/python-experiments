num = 0
largest = None
smallest = None
while num != 'done' :
    num = input('Enter a number: ')
    try:
        num = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None or num > largest :
        largest = num
    if smallest is None or num < smallest :
        smallest = num
print('Maximum:',largest)
print('Minimum:',smallest)
