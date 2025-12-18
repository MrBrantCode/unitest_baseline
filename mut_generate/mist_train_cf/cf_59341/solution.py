"""
QUESTION:
Create a function called `mandelbrot_set` that generates a 3D Mandelbrot fractal pattern. The function should take in the following parameters: `xmin`, `xmax`, `ymin`, `ymax`, `width`, `height`, and `maxiter`. The function should return a 3D scatter plot of the Mandelbrot fractal based on the given parameters. The `maxiter` parameter determines the depth of recursion. The output should be in the form of three arrays: `X_set`, `Y_set`, and `Z_set`, where `X_set` and `Y_set` represent the x and y coordinates of the points, and `Z_set` represents the z coordinates or the color of the points.
"""

import numpy as np

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[mandelbrot(complex(r, i),maxiter) for r in r1] for i in r2]))

def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return maxiter