from matplotlib import pyplot as plt
import os.path


def plot_profile(x, y, dataname):
    plt.plot(x, y)
    plt.savefig(os.path.join("plots", dataname))
    plt.show()


def plot_timeseries(x, y1, y2, dataname):
    plt.plot(x, y1)
    plt.savefig(os.path.join("plots", dataname + "_T"))
    plt.show()
    plt.plot(x, y2)
    plt.savefig(os.path.join("plots", dataname + "_p"))
    plt.show()
