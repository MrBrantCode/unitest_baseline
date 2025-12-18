"""
QUESTION:
Write a function named `compute_median` that takes four numeric inputs `x`, `y`, `z`, and `w`, and returns their median value. The function should work for any four numeric inputs.
"""

def compute_median(x, y, z, w):
    values = [x, y, z, w]
    values.sort()

    mid = len(values) // 2
    if len(values) % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2   # if even number of elements, return average of middle two
    else:
        return values[mid]  # if odd number of elements, return the middle one