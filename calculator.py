"""
calculates all values
"""

import numpy as np


def grad(depth, T):
    grads = []

    for i in range(0, len(T)-1):
        dT = T[i+1] - T[i]
        dh = depth[i+1] - depth[i]
        #print("dh: ", dh)
        grad = dT / dh
        grads.append(grad)

    #print(grads)
    grads_mean = np.mean(grads)
    #print(grads_mean)
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
