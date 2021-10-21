"""
Shows what happens in fft_basics_for_henri.py
"""


import fft_basics_for_henri


def main():
    signal, n, dt, t = fft_basics_for_henri.fake_signal()
    spectrum, f, df = fft_basics_for_henri.fft(signal, n, dt)
    fft_basics_for_henri.small_subplot(n, t, signal)
    fft_basics_for_henri.fft_tapered(n, f, signal, df, spectrum)


if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
