import sys

numbers = sys.argv[1:]
for i in range(len(numbers)):
  numbers[i] = int(numbers[i])


num =[]
for number in numbers:
    if number % 2 == 0:
      num.append("even")
    else:
      num.append("odd")
print(num)
