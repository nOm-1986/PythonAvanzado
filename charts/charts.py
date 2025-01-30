import matplotlib.pyplot as pylot
import matplotlib.animation as animation
import random as r

def generate_pie_chart():
    labels = [x for x in 'ABCDEFG']
    values = [r.randint(1, 200) for x in range(0, len(labels))]
    fig, ax = pylot.subplots()
    ax.pie(values, labels=labels)
    pylot.savefig('./pie_chart.png')
    pylot.close()

