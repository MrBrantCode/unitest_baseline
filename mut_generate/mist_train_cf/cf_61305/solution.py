"""
QUESTION:
Create a function called `substitute_in_array` that takes a multidimensional array, an original value, and a new value as input, and returns the modified array with the original value replaced by the new value, along with the number of substitutions made. The input array may be a list of lists.
"""

import numpy as np

def substitute_in_array(array, original_value, new_value):
    array = np.array(array)  
    mask = array == original_value  
    array[mask] = new_value  
    count = np.sum(mask)  
    return array.tolist(), count