fname = input('Enter a file name: ')

fhand = open(fname)

counts = dict()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in counts:
            counts[words[2]] = 1
        else:
            counts[words[2]] += 1

print(counts)
