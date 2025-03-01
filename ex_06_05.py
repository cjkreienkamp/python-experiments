str = 'X-DPSAM-Confidence:0.8475'

colpos = str.find(':')
aftcol = str[colpos+1:]
number = float(aftcol)

print('str: ',str)
print('num: ', number)
