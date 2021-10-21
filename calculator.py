"""
calculates all values
"""

import numpy as np


def grad(depth, T):
    grads = []

    for i in range(0, len(T)-1):
        dT = T[i+1] - T[i]
        dh = depth[i+1] - depth[i]
        grad = dT / dh
        grads.append(grad)

    grads_mean = np.mean(grads)
    return grads_mean


def eta(T_or_p):
    etas = []
    for i in T_or_p:
        eta = i - np.mean(T_or_p)
        etas.append(eta)
    return etas

