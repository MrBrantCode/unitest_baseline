"""
QUESTION:
Write a Python function `trapezoidal_prism_distance` that takes four parameters: `volume`, `height`, `base1`, and `base2`. The function should calculate and return the distance between the parallel bases of a trapezoidal prism given its volume, height, and the lengths of its bottom and top bases. The volume formula for a trapezoidal prism is Volume = 1/2 * (base1 + base2) * height * distance.
"""

def trapezoidal_prism_distance(volume, height, base1, base2):
    return volume / ((1/2) * (base1 + base2) * height)