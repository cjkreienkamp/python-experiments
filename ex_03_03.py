x = input('Enter score between 0.0 and 1.0: ')
try:
    x = float(x)
except:
    print('Error, please enter numeric input')
    quit()
if x > 1.0 or x < 0.0:
    print('Error, please enter a value within the range')
    quit()
elif x >= 0.9:
    print('Grade: A')
elif x >= 0.8:
    print('Grade: B')
elif x >= 0.7:
    print('Grade: C')
elif x >= 0.6:
    print('Grade: D')
else:
    print('Grade: F')
#  within the range')
