try:
    fname = input('Enter a file name: ')
except:
    print('Enter a proper file foo!')
    quit()

fhand = open(fname)
new_dict = dict()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    col_pos = words[5].find(':')
    hour = words[5][:col_pos]

    if hour not in new_dict:
        new_dict[hour] = 1
    else:
        new_dict[hour] += 1

lst = list()

for key, val in list(new_dict.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
