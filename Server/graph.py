import numpy as np
import matplotlib.pyplot as plt
from csv import reader
import csv
from matplotlib.pyplot import figure
from pylab import rcParams
from sklearn.cluster import k_means

def drawGraph(date, effect, hours):
    hour = max(hours)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes

    ax.set_title(date)
    ax.set_ylabel('Effect')
    ax.set_xlabel('Hour')
    ax.plot(hours,effect)
    ax.set_xticks([0, 8, 16, 23])
    ax.set_xticklabels([0,8,16,23])
    plt.grid()
    plt.plot(hours, effect)
    path = './static/uploads/date-effect.png'
    plt.savefig(path)
    return path