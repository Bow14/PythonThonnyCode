
string = input()

def FirstandLast(string):
  for i in range(len(string)):
    
    if i == 0:
      print(string[1], end = "")
    
    if i == len(string) - 1:
       print(string[i], end = "")
      
    if string[i] == '':
      print(string[i -1],
            string[i + 1], end = "")
      
print(FirstandLast(string))

#almost worked pog