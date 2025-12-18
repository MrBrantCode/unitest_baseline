"""
QUESTION:
Create a function named `draw_fractal` that generates a Mandelbrot set fractal based on the given parameters. The function should take in the minimum and maximum x and y values (`x_min`, `x_max`, `y_min`, `y_max`) that define the view frame, the width and height of the fractal image in pixels, and the maximum number of iterations (`max_iter`) as input. It should return three values: the x and y coordinates of the pixels in the fractal image, and a 2D array representing the number of iterations taken for each point to escape the Mandelbrot set. The function should use the Mandelbrot set formula to calculate the number of iterations for each point.
"""

import numpy as np

def draw_fractal(x_min, x_max, y_min, y_max, width, height, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter