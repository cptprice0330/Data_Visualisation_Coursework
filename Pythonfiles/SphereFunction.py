from numpy import *
def draw_sphere(xCen,yCen,zCen,radius):
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
            x = outer(radius*cos(theta),sin(phi))+xCen
            break
        except:
            print("Oops, bad exception starting again")
    while True:
        try:
            y = outer(radius*sin(theta),sin(phi))+yCen
            break
        except:
            print("Oops, bad exception starting again")
    while True:
        try:
            z = outer(ones(500),radius*cos(phi))+zCen
            break
        except:
            print("Oops, bad exception starting again")
    return (x,y,z)

def single_Shpere_plot(radius):
    import matplotlib.pyplot
    (x,y,z) = draw_sphere(radius)
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
    figure.plot_surface(x,y,z,color = (red,green,blue,alpha))
    matplotlib.pyplot.draw()
    matplotlib.pyplot.show()

def multiSpherePlot(size):
    import matplotlib.pyplot
    from mpl_toolkits.mplot3d import Axes3D
    xCen = 1
    yCen = 0
    zCen = 0
    data = matplotlib.pyplot.figure()
    ax = data.add_subplot(111, projection ='3d')

    for i in range(size):
        for j in range(size):
            for k in range(size):
                (xPlt,yPlt,zPlt) = draw_sphere(xCen+(i*size),yCen+(j*size),zCen+(k*size),(size*0.2))
                ax.plot_surface(xPlt,yPlt,zPlt,color = 'red')

    matplotlib.pyplot.draw()
    matplotlib.pyplot.show()

def compoundPlot(cCx,cCy,cCz,scalingF,size,ax): #takes center of the sodium chloride compound and builds visualiseation around
    import matplotlib.pyplot
    from mpl_toolkits.mplot3d import Axes3D
    (xPlt,yPlt,zPlt) = draw_sphere(cCx,cCy,cCz,size*0.2)
    ax.plot_surface(xPlt,yPlt,zPlt,color = 'red')
    (xPlt, yPlt, zPlt) = draw_sphere(cCx+scalingF,cCy,cCz, size * 0.1)
    ax.plot_surface(xPlt, yPlt, zPlt, color='blue')
    (xPlt, yPlt, zPlt) = draw_sphere(cCx,cCy+scalingF,cCz, size * 0.1)
    ax.plot_surface(xPlt, yPlt, zPlt, color='blue')
    (xPlt, yPlt, zPlt) = draw_sphere(cCx,cCy,cCz+scalingF, size * 0.1)
    ax.plot_surface(xPlt, yPlt, zPlt, color='blue')
    (xPlt, yPlt, zPlt) = draw_sphere(cCx-scalingF,cCy,cCz, size * 0.1)
    ax.plot_surface(xPlt, yPlt, zPlt, color='blue')
    (xPlt, yPlt, zPlt) = draw_sphere(cCx,cCy-scalingF,cCz, size * 0.1)
    ax.plot_surface(xPlt, yPlt, zPlt, color='blue')
    (xPlt, yPlt, zPlt) = draw_sphere(cCx,cCy,cCz-scalingF, size * 0.1)
    ax.plot_surface(xPlt, yPlt, zPlt, color='blue')



def sodiumPlot(size):
    import matplotlib.pyplot
    from mpl_toolkits.mplot3d import Axes3D
    xCen = 0
    yCen = 0
    zCen = 0
    data = matplotlib.pyplot.figure()
    ax = data.add_subplot(111, projection ='3d')
  #  compoundPlot(xCen,yCen,zCen,0.5,size,ax)
    for i in range (2,size,2):
        for j in range (2,size,2):
            for k in range (2,size,2):
                compoundPlot(xCen+i,yCen+j,zCen+k,2,size,ax)
    matplotlib.pyplot.draw()
    matplotlib.pyplot.show()
