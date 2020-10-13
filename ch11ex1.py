import re

fname = input('Enter a file name:')

fhand = open(fname)

find_exp = input('Enter a regular expression: ')

count = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall(find_exp, line)
    if len(x) > 0 :
        count += 1

print(fname, ' had %d lines that matched ' % count, find_exp)
