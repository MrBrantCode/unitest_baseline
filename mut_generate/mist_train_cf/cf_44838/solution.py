"""
QUESTION:
Write a function `kernel_density_estimation` that takes in a list of unique points `Xi` and returns a kernel density estimation where the value `Yi` is equivalent to `1/n` at each unique point `Xi` in the dataset.
"""

def kernel_density_estimation(points):
    n = len(points)
    return [(point, 1/n) for point in points]