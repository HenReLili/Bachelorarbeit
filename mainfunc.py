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
    dt = time[-1]/len(time)
    fft_basics_for_henri.fft(np.add(eta_T, eta_p), len(eta_T)-2, dt, "fft_eta")
    print("len: ", len(eta_T))
#    for j in range(0, int((len(eta_T)-128)/10+1)):
#        print("von ", 10*j, " bis ", 128+10*j)
#        fft_basics_for_henri.fft_tapered(128, np.add(eta_T, eta_p)[10*j:128+10*j], dt, "tapered_fft_eta_{number}".format(number=j),True)
#    print("all datapoints")
    fft_basics_for_henri.fft_tapered(len(eta_T), np.add(eta_T, eta_p), dt, "tapered_fft_eta", 1)
    eta_flatened = calculator.eta_flatened(eta_T, eta_p)
    fft_basics_for_henri.fft_tapered(128, eta_flatened, dt, "tapered_fft_eta", 2)


if __name__ == "__main__":
    main()
