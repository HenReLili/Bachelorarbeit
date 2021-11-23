"""
calculates all values
"""

import numpy as np
from scipy.optimize import curve_fit


def func(x, a, b):
    return 10**3*a*x+10**3*b

def linfit(p, T):
    p_new = []
    T_new = []
    for i in range(0, len(p)):
        if p[i] < -750:
            p_new.append(p[i])
            T_new.append(T[i])
    linear_model = np.polyfit(T_new,p_new,1)
    p_of_T = np.poly1d(linear_model)
    T_new = np.linspace(T_new[0], T_new[-1], num=6)
    p_new = np.linspace(p_of_T(T_new[0]), p_of_T(T_new[-1]), num=6)
    """print("type: ", type(p), type(p_new))
    popt, pcov = curve_fit(func, T_new, p_new, bounds=([0, -10], [2.5, 0]))
    print("fit: ", popt)
    for j in range(0, len(p_new)):
        p_new[j] = 10**3 * (popt[0] * T_new[j] + popt[1])
    # p_new = popt[0] * T_new + popt[1]"""
    return p_new, T_new


def grad(depth, T):
    grads = []

    f = open("test.txt", "w")
    for i in range(0, len(T)-1):
        dT = T[i+1] - T[i]
        dh = depth[i+1] - depth[i]
        grad = dT / dh
        f.write("{b}: {a}\n".format(a=grad, b=depth[i]))
        grads.append(grad)

    grads_mean = np.mean(grads)
    return grads_mean


def eta(T_or_p):
    etas = []
    for i in T_or_p:
        eta = i - np.mean(T_or_p)
        etas.append(eta)
    return etas


def eta_flatened(eta_T, eta_p):
    eta_flatened = np.add(eta_T, eta_p)[0:128]
    for j in range(1, int((len(eta_T)-128)/10+1)):
        eta_flatened = np.add(np.add(eta_T, eta_p)[10*j:128+10*j], eta_flatened)
    eta_flatened = eta_flatened/int((len(eta_T)-128)/10+1)
    return eta_flatened
