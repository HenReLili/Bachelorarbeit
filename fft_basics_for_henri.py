"""
Created on Sun Oct 17 13:20:20 2021

@author: simon
"""


import numpy as np
import matplotlib.pyplot as plt
import os.path


def fake_signal():
    # create fake signal
    n = 600     # length of signal
    dt = 1/800   # sampling interval [seconds]

    t = np.linspace(0, n*dt, n, endpoint=False)  # time axis of signal

    # the signal is just two sine waves with 50 and 80 Hz frequency
    signal = np.sin(50.0 * 2.0*np.pi*t) + 0.5*np.sin(80.0 * 2.0*np.pi*t)

    # let's have a look at the signal
    plt.figure(1)
    plt.plot(t, signal)
    plt.xlabel("time [s]")
    plt.ylabel("signal")
    return signal, n, dt, t


def fft(signal, n, dt, dataname):
    # calculate rfft (real fast fourier transform)
    fft_coeffs = np.fft.rfft(signal)    # fourier coefficients
    df = 1 / n / dt                   # sampling frequency

    # the factor of 2 comes from the symmetry of the Fourier coeffs
    spectrum = 2.*(fft_coeffs*fft_coeffs.conj()).real / df / n**2  # <- this is your spectrum!

    # calculate new x-axis (frequency space)
    f = df*np.arange(n/2. + 1)

    # let's have a look at the spectrum
    plt.figure(2)
    plt.ylim(min(spectrum[1:])/10, max(spectrum)*10)
    plt.loglog(f, spectrum)
    plt.xlabel("frequency f [s$^{-1}$]")
    plt.ylabel("PSD")
    plt.savefig(os.path.join("plots", dataname))
    plt.show()
    # plt.axvline(80, c="grey")
    # plt.axvline(50, c="grey")


########### THE REST DOWN BELOW IS NOT IMPORTANT IN THE BEGINNING ###########


# usually, the signal is "tapered", i.e. you apply a window function

# here I will just give you a taper function that you can use
def sin2_taper(N, frac):
    tape = np.ones(N)
    i = int(np.ceil(frac*N))
    if (i > N/2):
        print("fraction too large or N too small, returning NaN")
        return np.zeros(N)*np.nan

    xi = np.linspace(0, 1, i+1)*np.pi*0.5
    tape[:i+1] *= np.sin(xi)**2
    tape[-i-1:] *= (np.sin(xi)**2)[::-1]
    return tape


def small_subplot(n, t, signal):
    # have a look at it (it basically makes a "wave package" out of our signal)
    plt.figure(3)
    plt.subplot(211)
    plt.plot(sin2_taper(n, 0.1))

    plt.subplot(212)
    plt.plot(t, signal*sin2_taper(n, 0.1))  # <- see how it looks like a package now! ;-)


def fft_tapered(n, signal, dt, dataname, plot_number):
    # now calculate a new spectrum with the tapered signal

    df = 1 / n / dt                   # sampling frequency
    # calculate new x-axis (frequency space)
    if n % 2:
        even = 0
    else:
        even = 1
    f = df*np.arange(n/2 + even)


    # you have to correct the spectrum for the use of the window function like this
    correction_factor = 1/n * np.sum(sin2_taper(n, 0.1)**2)

    signal_win = signal * sin2_taper(n, 0.1)

    fft_coeffs_win = np.fft.rfft(signal_win)    # fourier coefficients like above

    # the factor of 2 comes from the symmetry of the Fourier coeffs
    spectrum_win = 2.*(fft_coeffs_win*fft_coeffs_win.conj()).real / df / n**2  # <- this is your spectrum!

    # calculates the inertial frequency
    #f_inert = 2 * 7.2921 * 10 ** (-5) * np.sin(latitude)

    # now plot the new spectrum
    plt.figure(plot_number)
    plt.ylim(min(spectrum_win[1:])/10, max(spectrum_win)*10)
    plt.loglog(f, spectrum_win, label="tapered")
    plt.savefig(os.path.join("plots", dataname))
    #plt.loglog(f, spectrum, label = "original")

    plt.legend()

    plt.xlabel("frequency f [s$^{-1}$]")
    plt.ylabel("PSD")
    # plt.axvline(80, c="grey")
    # plt.axvline(50, c="grey")


# do you see what happens? you get some weird oscillation, but - which is more
# important - you get less energy in the "wrong" frequencies. All the energy
# should be in the frequencies 50 and 80 (in the peaks), everything else is bad

# So the taper "helps" to reduce the amplitudes of the bad frequencies.
