import turtle 

def draw_square(tut, width):
    tut.fillcolor('green')
    tut.begin_fill()
    for i in range(4):
        tut.forward(width)
        tut.right(90)
    tut.end_fill()
    

def main():
    '''
    Program starts here.
    '''
    try:
        width = int(input("Enter your width: "))
        height = int(input("Enter your height: "))

        pass
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return

    tut = turtle.Turtle()
    draw_square(tut,width)
    
    tut.pu()
    tut.goto(25,25)
    tut.pd()



    


    pass
   
   
   

    
  

if __name__ == "__main__":
    main()
