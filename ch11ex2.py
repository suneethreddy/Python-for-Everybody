import re


rev = []

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()

count = 0
for line in fhand:
    line = line.rstrip()
    rev_temp = re.findall('^New Revision: ([0-9.]+)', line)
    for val in rev_temp:
        count += 1
        val = float(val)
        rev.append(val)
rev_sum = sum(rev)

rev_ave = rev_sum / count
average = int(rev_ave)
print(average)
