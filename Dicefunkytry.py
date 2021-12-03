from random import choice
import turtle
from turtle import Screen
import math
from statistics import mean

#Setting up Turtle
height = 1000
width = 1000
screen = Screen()
screen.setup(width, height)
bo = turtle.Turtle()


walks = 50
length = 200
Pa = [(0,1),(1,0),(0,-1),(-1,0)]
Mi_ma = [(-1, 0),(0,1),(1,0),(0,-2)]
Reg = [(-1,0),(1,0)]
end_points = []
   
def data(walks, length, steps, pen_color, pen_shape):
    #end_points = []
    #for each walk of 1000 steps, find the endpoint, add to list
    for i in range(walks):
        point = [0,0]
        for j in range(length):
            #point = list(map(sum,zip(point,choice(steps)))
            turtle.update()
            step = choice(steps)
            point[0] += step[0]
            point[1] += step[1]
        end_points.append(point)
    
    
def plot(walks, pen_color, pen_shape):
    bo.color(pen_color)
    bo.shape(pen_shape)
    bo.shapesize(0.5, 0.5)
    data = walks
    print(data)
    
    
    for i in range(len(data)):
        bo.pu()
        bo.goto(data[i])
        bo.stamp()
        if i > 50:
            bo.color("green")
            bo.shape("square")
        if i > 100:
            bo.color("red")
            bo.shape("triangle")
            
        
        
        
    bo.screen.mainloop()
   
    #draw the endpoints to the canvas
    #bo.pu()
    #for point in end_points:
        #bo.goto(point[0],point[1])
        #bo.stamp()
    #bo.screen.mainloop()

def stimulate(walks, length, steps):
    point = [0,0]
    end_points.append(point)
    #end_points = []
   
    #for each walk of 1000 steps, find the endpoint, add to list
    for i in range(walks):
        point = [0,0]
        for j in range(length):
            #point = list(map(sum,zip(point,choice(steps)))
            step = choice(steps)
            point[0] += step[0]
            point[1] += step[1]
        end_points.append(point)
    return(end_points)

    #Math from distance from origin endpoints
    distance = []
    for point in end_points:
        dist = math.sqrt(point[0]**2 + point[1]**2)
        distance.append(dist)
    # calculate average walk length
    print(f'\nAverage walk length: {mean(distance)}')
    print(f'\nMax =: {max(distance)}')
    print(f'\nMin =: {min(distance)}')

   

def main():
    Pa_plot = stimulate(walks, length, Pa)
    print(Pa_plot)
    #plot(Pa_plot, "black", "circle")
    Ma_plot = stimulate(walks, length, Mi_ma)
    print(Ma_plot)
    #plot(Ma_plot, "green", "square")
    Reg_plot = stimulate(walks, length, Reg)
    print(Reg_plot)
    plot(Reg_plot, "black", "circle")
  
   
if __name__ == '__main__':
    main()