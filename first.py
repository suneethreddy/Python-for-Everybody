print('Hey there!')

name = input('What is your name?\n')
print('Hello '+name+'\n')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()


fruit = 'apple'

index = 0
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1

print('\n')

index=len(fruit)-1
while index>=0:
    letter=fruit[index]
    print(letter)
    index=index-1
