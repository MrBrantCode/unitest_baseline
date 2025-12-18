"""
QUESTION:
Create a function named `split_array` that takes a list of numbers as input and partitions it into three sections where each section's cumulative product is uniform. The function should return the three sections if such a partition exists; otherwise, it should return "No split possible".
"""

import numpy as np
def split_array(array):
    for i in range(1, len(array)):
        for j in range(i+1, len(array)):
            part1 = array[:i]
            part2 = array[i:j]
            part3 = array[j:]
            
            product1 = np.prod(part1)
            product2 = np.prod(part2)
            product3 = np.prod(part3)
            if product1 == product2 == product3:
                return part1, part2, part3
    return "No split possible"