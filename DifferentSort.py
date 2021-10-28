import csv

def better_sort(line):
    line_parameters = line.strip().split(',')
    quanity = (line_parameters[0])
    
    return quanity

fp = open('LegendsData.csv')
contents = fp.readlines()

contents.sort(key=better_sort)

for line in contents:
    print(line)
    
fp.close()