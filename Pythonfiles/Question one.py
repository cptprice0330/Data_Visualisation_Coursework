from numpy import *
import plotly

theta = linspace(0,2*pi,500)
phi = linspace(0,pi,500)
# theta and phi are 500 angles in radians between 0 and 2pi and 0 and pi respectivly, these are used to create the points on the sphere to plot.

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
print(radius)
print(y)
#Plotting

data = plotly.graph_objs.Data([ plotly.graph_objs.Surface(
        x=x,
        y=y,
        z=z
    )])
layout = plotly.graph_objs.Layout(
    title='Bloch sphere',
    autosize=False,
    width=1000,
    height=1000,
    showlegend = False,
    margin=plotly.graph_objs.Margin(
        l=65,
        r=50,
        b=65,
        t=90))
fig = plotly.graph_objs.Figure(data=data, layout=layout)

plotly.offline.plot(fig, filename = 'SphereTest.html')