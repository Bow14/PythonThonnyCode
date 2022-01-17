word = 'pobilitiyy'
count = 0
for letter in word:
    if letter == 'i':
        count  = count + 1
    elif letter == 'y':
        count = count + 2
    
print(count)