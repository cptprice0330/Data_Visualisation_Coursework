# G:\pycharm\Projects\Data_Visualisation_Coursework\Textfiles\stmData.txt

from matplotlib import pyplot
import numpy as np


d = np.genfromtxt("G:\pycharm\Projects\Data_Visualisation_Coursework\Textfiles\stmData.txt", delimiter=" ")[:,:-1]
#n, bins, patches = pyplot.hist(d, 50, normed=1, facecolor='m', alpha=0.75)


pyplot.imshow(d,origin="Center",cmap="Greens")
pyplot.colorbar()
pyplot.show()

