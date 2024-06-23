# majdooron ko bulawa
import matplotlib.pyplot as plt


class Graph:

    def graph(self, x, y, lbl="data"):
        plt.plot(x, y, label=lbl)

    def show(self):
        plt.show()
