def computegrade(x):
    if x > 1.0 or x < 0.0:
        grade = 'Bad score'
    elif x >= 0.9:
        grade = 'A'
    elif x >= 0.8:
        grade = 'B'
    elif x >= 0.7:
        grade = 'C'
    elif x >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade

x = input('Enter score: ')
try:
    x = float(x)
except:
    print('Bad score')
    quit()
print(computegrade(x))
