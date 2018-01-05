from math import exp
from numpy import sum
from matplotlib import pyplot
from numpy import random
random.seed(5)
from numpy.matlib import empty


def arrayEnergy(array):
    x = 0
    for i in range(0, 19):
        for j in range(0, 19):
            #if i == 19 and j == 19:
            #    break
            #elif i == 19:
            #    x += array[i,j]*array[i,j+1]
            #elif j == 19:
            #    break
                #x += array[i,j]*array[i+1,j]
                #x += array[i+1][j-1]
            #elif i == 0:
                x += array[i,j]*array[i+1,j]
                x += array[i,j]*array[i,j+1]
                #x += array[i+1][j+1]
            #else:
                #x +=array[i,j]* array[i+1,j]
                #x += array[i,j]*array[i,j+1]
                #x += array[i+1][j-1]
                #x += array[i+1][j-1]
    E = -1*x
    return E

def changeState(State):
    #arraySelector = random.randint(1,4001)
    #if arraySelector <= 20:
    #    flippedSpin = arraySelector*100
    #else:
    #a = arraySelector//21
    #while arraySelector > 20:
    #    arraySelector -= 20
    #b = arraySelector*100
    #flippedSpin = a+b
    i = random.randint(0,19)
    j  = random.randint(0,19)
    State[i,j] *= -1
    #if State[i,j] == 1:
    #    State[i,j] = -1
    #else:
    #    State[i,j] = 1

    return State

def checkState(oldState):
    newState = changeState(oldState)
    eDiff = arrayEnergy(newState)-arrayEnergy(oldState)
    #if arrayEnergy(newState) < arrayEnergy(oldState):
        #pAlpha = 1
    #else:
    #    pAlpha = exp(eDiff/1)
    #if pAlpha < 1:
    #    finalState = newState
    #else:
    #    finalState = oldState
    if eDiff>0:
        if random.rand()<exp(-1*eDiff):
            finalState = newState
            t = sum(finalState)
        else:
            finalState = oldState
    else:
        finalState = newState
        t = sum(finalState)
    #print(finalState)
    return finalState,t


def print20x20(array):  # prints the 20x20 row by row rather than as a single line
    for i in range(0, 20):
        print(array[i])


z = 0
m = empty((20,20),int)
mplot = []
# creates the 20x20 canvas
for i in range(0, 20):
#    m.append([])
    for j in range(0, 20):
#        # m[i].append([])
        x = random.rand()
        if x > 0.5:
            m[i,j] = -1
        else:
            m[i,j] = 1
z = sum(m[i,0])  # Counts to check net magnetization
#print20x20(m)
print(m)
print(z)
total = sum(m)
print(total)
print()
print(arrayEnergy(m))
for count in range(0,10000):
    m,total = checkState(m)
    mplot.append(total)
print(arrayEnergy(m))
print(mplot)
#n, bins, patches = pyplot.hist(m, 50, normed=1, facecolor='m', alpha=0.75)
pyplot.plot(mplot)
#pyplot.imshow(m,origin="Center",cmap="Greens")
#pyplot.colorbar()
pyplot.show()
