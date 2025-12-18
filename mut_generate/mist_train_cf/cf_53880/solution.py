"""
QUESTION:
Write a function `julia_set` that generates a 3-dimensional fractal pattern based on the provided parameters. The function should take in a complex number `c`, the limits of the x, y, and z axes `xlim`, `ylim`, and `zlim`, the resolution `res` of each axis, and the maximum number of iterations `iter`. The function should return a 3D array representing the fractal pattern.
"""

import numpy as np

def julia_set(c, xlim, ylim, zlim, res, iter):
    x = np.linspace(xlim[0], xlim[1], res[0])
    y = np.linspace(ylim[0], ylim[1], res[1])
    z = np.linspace(zlim[0], zlim[1], res[2])
    fractal = np.empty((res[0],res[1],res[2]))

    for i in range(res[0]):
        for j in range(res[1]):
            for k in range(res[2]):
                a, b, d = x[i], y[j], z[k]
                for t in range(iter):
                    a, b, d = a*a - b*b - d*d + c.real, 2*a*b + c.imag, 2*a*d
                    if a*a + b*b + d*d > 4.0:
                        break
                fractal[i,j,k] = t

    return fractal