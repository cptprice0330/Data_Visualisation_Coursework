from math import exp

from matplotlib import pyplot
from numpy import sum
from numpy import random

from numpy.matlib import empty

random.seed(5)


def energyCalc(array):
    x1 = 0
    x2 = 0
    x3 = 0
    for i in range(1, 20):
        for j in range(1, 20):
            x1 += array[i - 1, j] * array[i, j]
            x2 += array[i, j - 1] * array[i, j]
    # for k in range (0,19):
    #   x3 += array[k,19]*array[k+1,19]

    e = -1 * (x1 + x2 + x3)
    return e


def checkState(old_state, i, j):
    t = 0
    old_energy = energyCalc(old_state)
    #print("*--")
    #print(old_energy)
    new_state = old_state
    new_state[i, j] = old_state[i, j] * -1
    e_diff = energyCalc(new_state) - old_energy
    #print("--")
    #print((energyCalc(new_state)))
    #print("--*")
    if e_diff > 0:
        if random.random() < exp(-1 * e_diff):
            final_state = new_state
            t = sum(final_state)
            #print(t)
        else:
            final_state = old_state
    else:
        final_state = new_state
        t = sum(final_state)
    # print(final_state)
    return final_state, t


m = empty((20, 20), int)
mplot = []
# creates the 20x20 canvas
for y in range(0, 20):
    #    m.append([])
    for z in range(0, 20):
        #        # m[i].append([])
        x = random.rand()
        if x > 0.5:
            m[y, z] = -1
        else:
            m[y, z] = 1

print(m)
print(sum(m))
print()
print(energyCalc(m))

for cycles in range(0, 100000):
    o = random.randint(0, 20)
    p = random.randint(0, 20)
    m, total = checkState(m, o, p)
    mplot.append(total)

print()
print(mplot)
print()
print(energyCalc(m))
pyplot.plot(mplot)
pyplot.show()
