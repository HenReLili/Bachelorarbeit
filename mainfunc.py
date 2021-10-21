"""
Executing the programm.
access-token: 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
"""


import plot
import readin
import calculator
import fft_basics_for_henri

import numpy as np


def main():
    for i in range(0, 2):
        p_prof, T_prof, dataname = readin.datareader_profile(i)
        plot.plot_profile(T_prof, p_prof, dataname)
        grad = calculator.grad(p_prof, T_prof)
        print("grad: ", grad)

    time, p_time, T_time, dataname = readin.datareader_timeseries()
    eta_T = calculator.eta(T_time/grad)
    eta_p = calculator.eta(p_time)
    plot.plot_timeseries(time, eta_T, eta_p, dataname)
    spectrum, f, df = fft_basics_for_henri.fft(np.add(eta_T, eta_p), len(eta_T)-2, time[-1]/len(time))
    fft_basics_for_henri.fft_tapered(len(eta_T), f, np.add(eta_T, eta_p), df, spectrum)


if __name__ == "__main__":
    main()
