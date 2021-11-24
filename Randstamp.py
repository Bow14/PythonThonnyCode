from random import choice
import turtle
import math
from statistics import mean

def main():
    length, walks = 1000, 50
    steps = [(0,1),(1,0),(0,-1),(-1,0)]
    bo = turtle.Turtle()
    end_points = []
    
    #for each walk of 1000 steps, find the endpoint, add to list
    for i in range(walks):
        point = [0,0]
        for j in range(length):
            step = choice(steps)
            point[0] += step[0]
            point[1] += step[1]
        end_points.append(point)

    
    #draw the endpoints to the canvas
    bo.pu()
    for point in end_points:
        bo.goto(point[0],point[1])
        bo.stamp()
    bo.screen.mainloop()
    
    #Math from distance from origin endpoints
    distance = []
    for point in end_point:
        dist = math.sqrt(point[0]**2 + point[1]**2)
        distance.append(dist)
    print(distance)
    
    
    
if __name__ == '__main__':
    main()