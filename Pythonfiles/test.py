from Pythonfiles import SphereFunction

SphereFunction.sodiumPlot(20) # size must be > 4 to plot more than one, size/4 is number of sodium atoms per side
# 6 minutes to run 16 with quick mode
import linecache




def arrayFromTextFile(File):
    data = open(File, "r")
    i = 0
    x = []
    x.append([])
    for line in data:
        line = line.strip()
        # print(line)
        # print()
        columns = line.split()
        # print(columns)
        x[i].append(columns)
        x.append([])
        i += 1
    return (x)
