import turtle

def circle(plasma,width):
 for i in range(4):
    plasma.forward(width)
    plasma.lt(80)

def main():
    bow_turtle = turtle.Turtle()
    bow_turtle.fillcolor('blue')
    bow_turtle.begin_fill()
    circle(bow_turtle, 200)
    
    
    
    
    
    
    
    bow_turtle.end_fill()
    
if __name__ == '__main__':
    main()