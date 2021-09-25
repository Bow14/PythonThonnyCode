for digit in range(1,9):
    for peeps in range(9-digit, 0, -1):
        print(".", end='')
    print(digit)