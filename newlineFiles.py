import sys

testbef = sys.argv[0]

with open(testbef, "r") as input_file:
    newline = input_file.readlines()
    newline.reverse()
    for newline in newline:
        print(newline)