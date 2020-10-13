fname = input('Enter file: ')

fhand = open(fname)

flist = []
for line in fhand:
    words = line.split()
    if len(words) == 0:
        continue
    for word in words:
        if word in flist:
            continue
        flist.append(word)
        flist.sort()
print(flist)
