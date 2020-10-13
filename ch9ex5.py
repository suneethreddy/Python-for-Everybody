try:
    fname = input('Enter a file name: ')
except:
    print('Missing or wrong file!')
    quit()

new_dict = dict()

fhand = open(fname)

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')
        domain = words[1][atpos+1:]
        if domain not in new_dict:
            new_dict[domain] = 1
        else:
            new_dict[domain] += 1

print(new_dict)
