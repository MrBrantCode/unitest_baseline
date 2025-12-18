"""
QUESTION:
Write a function `hypercube_volume` that calculates the volume of a 4-dimensional hypercube given the length of its side. The volume of the hypercube is calculated as `s^n`, where `s` is the side length and `n` is the dimensionality of the space (in this case, `n=4`).
"""

def hypercube_volume(side_length):
    return side_length ** 4