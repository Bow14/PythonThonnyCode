import random
import turtle
import math
from statistics import mean

black = [(-1,0),(0,1),(0,-1),(-1,0)] #Pa
#green = [(-1,0)(0,1)(1,0)(0,2)] #Mi-Ma
#red = [(-1,0),(1,0)] #Reg

bo = turtle.Turtle()

def stimulate():
    length, walk = 1000,50
    final_points = []
    for i in range(walk):
        point = [0,0]
        for p in range(length):
          step = choice(black,green,red)
          point[0] += step[0]
          point[1] += step[1]
          final_points.append(point)
        bo.pu()
        for point in final_points:
            bo.goto(point[0],point[1])
            bo.stamp()
            bo.screen.mainloop()
    
    print(final_points)
    




def main():









    if __name__ == '__main__':
        main()
