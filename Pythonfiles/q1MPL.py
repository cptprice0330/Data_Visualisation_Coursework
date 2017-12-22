from numpy import *
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
theta = linspace(0,2*pi,500)
phi = linspace(0,pi,500)
# theta and phi are 500 angles in radians between 0 and 2pi and 0 and pi respectivly, these are used to create the points on the sphere to plot.
red = 110
green = 110
blue = 110
alpha = 110
random.seed(679)
while True:
    try:
        radius = int(input("Enter the radius you wish for your sphere:\n"))
        break
    except ValueError:
        print("Not a valid numerical integer")
while True:
    try:
        x = outer(radius*cos(theta),sin(phi))
        break
    except:
        print("Oops, bad exception starting again")
while True:
    try:
        y = outer(radius*sin(theta),sin(phi))
        break
    except:
        print("Oops, bad exception starting again")
while True:
    try:
        z = outer(ones(500),radius*cos(phi))
        break
    except:
        print("Oops, bad exception starting again")

if (input("colours or random colour:? \n") == 'colours'):
    while red > 101:
        try:
            red = int(input("Enter a red value"))
        except:
            print("FUCKED")
    while green > 101:
        try:
            green = int(input("Enter a green value"))
        except:
            print("FUCKED")
    while blue > 101:
        try:
            blue = int(input("Enter a blue value"))
        except:
            print("FUCKED")
    while alpha > 101:
        try:
            alpha = int(input("Enter a alpha(opacity) value"))
        except:
            print("FUCKED")
else:
        print("Picking random")
        red = random.randint(1,100)
        blue = random.randint(1,100)
        green = random.randint(1,100)
        alpha = random.randint(1,100)

red/=100
blue/=100
green/=100
alpha/=100

data = matplotlib.pyplot.figure(figsize = (10,10))
figure = data.gca(projection = '3d')
fig = data.add_subplot(100,projection = '3d')
figure.plot_surface(x,y,z,color = (red,green,blue,alpha))
matplotlib.pyplot.draw()
matplotlib.pyplot.show()


