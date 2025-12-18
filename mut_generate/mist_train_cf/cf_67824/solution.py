"""
QUESTION:
Implement a function called `unique_elements_3D` that takes a 3D array as input and returns a dictionary with keys 'x', 'y', and 'z'. The values corresponding to these keys should be lists of numbers that appear only once in each of the sub-arrays of the input 3D array, where 'x', 'y', and 'z' represent the first, second, and third sub-arrays respectively.
"""

from collections import Counter

def unique_elements_3D(arr):
    unique_elements = {'x': [], 'y': [], 'z': []}
    
    for i in range(len(arr)):
        flat_list = [item for sublist in arr[i] for item in sublist]
        count = Counter(flat_list)
        unique = [k for k, v in count.items() if v == 1]
        unique_elements['x'].extend(unique) if i == 0 else unique_elements['y'].extend(unique) if i == 1 else unique_elements['z'].extend(unique)
    
    return unique_elements