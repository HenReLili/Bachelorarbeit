"""
Executing the programm.
"""

import plot
import readin


def main():
    for i in range(0, 2):
        p, T, dataname = readin.datareader_profile(i)
        plot.plot_profile(T, p, dataname)


    time, p, T, dataname = readin.datareader_timeseries()
    plot.plot_timeseries(time, T, p, dataname)


if __name__ == "__main__":
    main()
