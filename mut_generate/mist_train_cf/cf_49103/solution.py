"""
QUESTION:
Create a function `mandelbrot_set` that generates a 2D representation of the Mandelbrot set based on given parameters. The function should take the following parameters: `width` and `height` for the output image, `zoom` and `x_off` and `y_off` for zooming and offsetting the fractal, and `max_iter` for the maximum number of iterations. The function should return a 2D array representing the Mandelbrot set.
"""

import numpy as np

def mandelbrot_set(width, height, zoom=1, x_off=0, y_off=0, max_iter=256):
    """Generates a Mandelbrot set.

    Parameters:
    width (int): The width of the output image.
    height (int): The height of the output image.
    zoom (float): The zoom level.
    x_off (float): The x offset.
    y_off (float): The y offset.
    max_iter (int): The maximum number of iterations.

    Returns:
    ndarray: A 2D array representing the Mandelbrot set.
    """
    pixels = np.arange(width*height, dtype=np.uint32).reshape(height, width)
    x = np.linspace(x_off - zoom, x_off + zoom, width)
    y = np.linspace(y_off - zoom, y_off + zoom, height)
    for x_index, x_value in enumerate(x):
        for y_index, y_value in enumerate(y):
            z, c = 0 + 0j, x_value + y_value*1j
            for iteration in range(max_iter):
                if abs(z) > 2:
                    break 
                z = z*z + c
            color = iteration << 21 | iteration << 10 | iteration*8
            pixels[y_index, x_index] = color
    return pixels