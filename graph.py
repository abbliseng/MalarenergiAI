from django import template

fileName = "MalarenergiAI\Python\Data\Hallsta\Data_Hallsta_vikt.csv"    

register = template.Library()  
    
@register.simple_tag
def drawGraph(file):
    import numpy as np
    import matplotlib.pyplot as plt
    from csv import reader
    import csv
    from matplotlib.pyplot import figure
    from pylab import rcParams
    from sklearn.cluster import k_means

    effect = []
    # temperature = []
    # day = []
    # month = []
    hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    data = csv.reader(open(file), delimiter=';')

    inputdate = input('åååå-mm-dd: ')

    date = inputdate[slice(4)] + ';' + inputdate[slice(5, 7)] + ';' + inputdate[slice(8, 11)]

    for i in data:
        for hour in hours:
        
            filedate = i[0] + ';' + i[1] + ';' + i[2]
            
            if date == filedate and hour == int(i[3]):
                ef = i[int(5)]
                ef = ef.replace(',', '.')
                ef = float(ef)
                effect.append(ef)


    hour = max(hours)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes

    ax.set_title(inputdate)
    ax.set_ylabel('effecten???')
    ax.set_xlabel('hours???')
    ax.plot(hours,effect)
    ax.set_xticks([0, 8, 16, 23])
    ax.set_xticklabels([0,8,16,23])
    plt.grid()
    # plt.plot(hours, effect)
    plt.savefig('date-effect.png')
    plt.show()

    return "hej"

drawGraph(fileName)

# plt.title('-_-')
# plt.ylabel('effect???')
# plt.xlabel('temperature???')
# plt.plot(temperature, effect, linestyle="", marker="o", markersize=0.8)
# plt.grid()
# plt.savefig('temperature-effect.png')
# plt.show()