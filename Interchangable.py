cool = input()

for i in cool:
    if i.islower():
        print("l", end = '')
    elif i.isupper():
        print('u', end = '')
    else:
        print('-', end = '')
        