"""
QUESTION:
Implement a function `generate_meshgrid` that generates a 2D grid of points using NumPy. The function should take in the center coordinates `xcen` and `ycen`, half ranges `xhalfrng` and `yhalfrng`, and the number of points along each axis `xnpts` and `ynpts`, and return the meshgrid of points as a tuple `(xx, yy)`, where `xx` and `yy` are 2D arrays representing the x-coordinates and y-coordinates of the grid points, respectively.
"""

import numpy as np

def generate_meshgrid(xcen, ycen, xhalfrng, yhalfrng, xnpts, ynpts):
    x = np.linspace(xcen - xhalfrng, xcen + xhalfrng, xnpts)
    y = np.linspace(ycen - yhalfrng, ycen + yhalfrng, ynpts)
    xx, yy = np.meshgrid(x, y)
    return xx, yy