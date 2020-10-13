fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'Good':
        print('day to you!')
        exit()
    print('Wrong or missing file!')
    exit()

total = 0
temp = 0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        temp = line.find(':')
        temp = line[temp + 1:]
        temp = float(temp)
        total = temp + total
average = total/count
print('Average spam confidence: ', average)
