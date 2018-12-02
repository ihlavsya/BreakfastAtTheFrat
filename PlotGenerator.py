import matplotlib.pyplot as plt


class PlotGenerator:
    def GetScatter(self, x, y, labelx, labely, label):
        plt.scatter(x, y)
        plt.title(labelx+' '+labely+' '+label, fontsize=14)
        plt.xlabel(labelx, fontsize=14)
        plt.ylabel(labely, fontsize=14)
        plt.grid(True)
        plt.show()

    def GetPlot(self, x, y, labelx, labely, label):
        plt.plot(x, y)
        plt.title(labelx+' '+labely+' '+label, fontsize=14)
        plt.xlabel(labelx, fontsize=14)
        plt.ylabel(labely, fontsize=14)
        plt.grid(True)
        plt.show()
