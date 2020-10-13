fname = input('Enter the file name: ')

fhand = open(fname)

count = 0
new_dict = dict()

for line in fhand:
    words = line.split()
    for word in words:
        count = count + 1
        if word in new_dict:
            continue
        new_dict[word] = count

if 'Python' in new_dict:
    print('True')
else:
    print('False')
