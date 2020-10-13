try:
    fname = input('Enter a file name: ')
except:
    print('Enter a proper file foo!')
    quit()

fhand = open(fname)
new_dict = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[1] not in new_dict:
            new_dict[words[1]] = 1
        else:
            new_dict[words[1]] += 1

lst = list()
for key, val in list(new_dict.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:1]:
    print(key, val)
