hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
hours = float(hours)
rate = float(rate)
if hours>40:
    pay = 40*rate + (hours-40)*rate*1.5
else:
    pay = 40*rate
print('Pay:',pay)
