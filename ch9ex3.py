mail_count = dict()
try:
    fname = input('Enter file name:')
except:
    print('Enter a proper file!')
    exit()

fhand = open(fname)

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in mail_count:
            mail_count[words[1]] = 1
        else:
            mail_count[words[1]] += 1

print(mail_count)
