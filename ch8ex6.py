my_list = []
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break
    try:
        number = float(input_number)
    except:
        print('Enter a damn number foo!')
        quit()

    my_list.append(number)

print('Maximum', max(my_list))
print('Minimum', min(my_list))
