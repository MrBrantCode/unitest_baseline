"""
QUESTION:
Create a function `create_meshgrid` that generates a meshgrid of variable dimensions. The function should take the number of dimensions as a variable `dim` and return a meshgrid of that dimension. The function should also accept optional parameters `start`, `stop`, and `num` to specify the range and number of points on each axis, defaulting to `-5`, `5`, and `5` respectively.
"""

import numpy as np

def create_meshgrid(dim=2, start=-5, stop=5, num=5):
    axes = [np.linspace(start, stop, num) for _ in range(dim)]
    return np.meshgrid(*axes, indexing='ij')