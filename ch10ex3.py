import string
try:
    fname = input('Enter a file name: ')
except:
    print('Enter a proper file foo!')
    quit()

fhand = open(fname)
new_dict = dict()
counts = 0

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in new_dict:
                new_dict[letter] = 1
            else:
                new_dict[letter] += 1

lst = list()

for key, val in list(new_dict.items()):
    lst.append((val / counts, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)
