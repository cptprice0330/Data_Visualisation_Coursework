from numpy import random


def arrayEnergy(array):
    for i in range(0, 20):
        for j in range(0, 20):
            x = x + array[i, j]
    E = -1(x)
    return E


def print20x20(array):  # prints the 20x20 row by row rather than as a single line
    for i in range(0, 20):
        print(array[i])


z = 0
m = []
# creates the 20x20 canvas
for i in range(0, 20):
    m.append([])
    for j in range(0, 20):
        # m[i].append([])
        x = random.rand()
        if x > 0.5:
            m[i].append(-1)
        else:
            m[i].append(1)
    z = z + m[i][0]  # Counts to check net magnetization
print20x20(m)
print(z)
