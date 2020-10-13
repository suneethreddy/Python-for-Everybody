str = 'X-DSPAM-Confidence:0.8475'

x=str.find(':')
y=str[x+1:]
y=float(y)
print(y)
print(type(y))
