"""
QUESTION:
Create a function called `mandelbrot_set` that generates a fractal pattern based on the Mandelbrot set, taking the following parameters: `width`, `height`, `zoom`, `x_off`, `y_off`, and `max_iter`. The function should return a 3D numpy array representing the image of the fractal pattern, where each pixel's color is determined by the iteration count in the Mandelbrot set calculation. The function should not display the image. The returned image should have a shape of `(height, width, 3)` and data type of `np.uint8`.
"""

import numpy as np

def mandelbrot_set(width, height, zoom=1, x_off=0, y_off=0, max_iter=256):
    """ Generate a fractal pattern based on the Mandelbrot set """
    
    # Create an image with desired resolution and color channels
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    for x in range(width):
        for y in range(height):

            # Calculate real and imaginary part of z
            zx, zy = (x - width / 2) / (0.5 * zoom * width) + x_off, (y - height / 2) / (0.5 * zoom * height) + y_off
            c = zx + zy * 1j
            z = c
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break 
                z = z * z + c

            # Use iteration count to decide the color
            r, g, b = i % 8 * 32, i % 16 * 16, i % 32 * 8
            image[y, x] = (b, g, r)
            
    return image