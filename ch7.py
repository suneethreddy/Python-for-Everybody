fname = input('Enter the name of file: ')
try:
    fhand = open(fname)
except:
    print('Wrong or missing file!')
    exit()

for line in fhand:
    line = line.upper()
    print(line)
