from random import choice
import turtle
import math
from statistics import mean


#green = [(-1,0)(0,1)(1,0)(0,2)] #Mi-Ma
#red = [(-1,0),(1,0)] #Reg

walks = 50
length = 100
Pa = [(0,1),(1,0),(0,-1),(-1,0)]
Mi_ma = [(-1, 0),(0,1),(1,0),(0,-2)]
Reg = [(-1,0),(1,0)]

def stimulate(walks, length, steps, pen_color, pen_shape):

    bo = turtle.Turtle()
    bo.color(pen_color)
    bo.shape(pen_shape)
    end_points = []

    #for each walk of 1000 steps, find the endpoint, add to list
    for i in range(walks):
        point = [0,0]
        for j in range(length):
            #point = list(map(sum,zip(point,choice(steps)))
            step = choice(steps)
            point[0] += step[0]
            point[1] += step[1]
        end_points.append(point)


    #draw the endpoints to the canvas
    bo.pu()
    for point in end_points:
        bo.goto(randint(-100,0), randint(0,100))
        bo.stamp()
    bo.screen.mainloop()
    #Math from distance from origin endpoints
    distance = []
    for point in end_points:
        dist = math.sqrt(point[0]**2 + point[1]**2)
        distance.append(dist)
    # calculate average walk length
    print(f'\nAverage walk length: {mean(distance)}')
    
def plot(walks, length,stimulate):
    stimulate(walks, length, Pa, "black", "circle")
    stimulate(walks, length, Mi_ma, "green", "square")
    stimulate(walks, length, Reg, "red", "triangle")

def main():

    plot(walks,length, stimulate)
    



if __name__ == '__main__':
    main()