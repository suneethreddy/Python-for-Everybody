import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

size = 0

while True:
    data = fhand.read(3000)
    if len(data) < 1: break
    size = size + len(data)
    if size < 3000:
        print(data.decode().strip())

print(size)
