'''
This entire part of this assignment took me a while to solve it and i dont know why
'''

def nested_sum(t): #calling down the list from main pretty much
    lyst = 0 #need something to base your start off of
    for nest in t: #The variable nest doesn't matter i can be anything as long as it matches
        lyst += sum(nest) #the adding part of the list
    return lyst #need the return function or it will print none im not exactly sure why
    
    
def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

if __name__ == '__main__':
    main()