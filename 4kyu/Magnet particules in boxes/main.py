import numpy as np


def doubles(maxk, maxn):
    res = 0
    for k in range(1, maxk + 1):
        res += np.sum(1 / (k * np.arange(2, maxn + 2,dtype=np.float64) ** (2 * k)))
    return res