def computepay(hours, rate):
    if hours>40:
        pay = 40*rate + (hours-40)*rate*1.5
    else:
        pay = 40*rate
    return pay
    
hours = input('Enter Hours: ')
try:
    hours = float(hours)
except:
    print('Error, please enter numeric input')
    quit()
rate = input('Enter Rate: ')
try:
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
print('Pay:',computepay(hours,rate))
