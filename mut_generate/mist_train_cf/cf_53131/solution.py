"""
QUESTION:
Write a function `find_min_disparity(arr)` that finds the minimum difference between any two elements within an array. The function should flatten nested arrays, ignore `None` and non-numeric elements, and consider strings containing numbers and boolean values. If the array is empty or has a single element, it should return the message 'Array should have at least two elements'.
"""

import numpy as np

def find_min_disparity(arr):
    """
    Function to find the minimum difference between any two elements within an array.
    Flatten nested arrays, ignore None and non-numeric elements,
    Convert strings containing numbers and consider boolean values.
    """

    def is_complex_num(n):
        try:
            complex(n)
            return True
        except ValueError:
            return False

    arr = np.array(arr)
    arr_ = arr.flatten().tolist()

    arr = [i for i in arr_ if isinstance(i, (int, float, complex)) or 
    (isinstance(i, str) and is_complex_num(i.strip())) or 
    (isinstance(i, bool))]

    arr = [complex(i) if isinstance(i, str) else int(i) if isinstance(i, bool) else i for i in arr]

    if len(arr) < 2:
        return 'Array should have at least two elements'

    arr.sort(key=abs)  
    min_disparity = abs(arr[1] - arr[0])

    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) < min_disparity:
            min_disparity = abs(arr[i] - arr[i-1])

    return min_disparity