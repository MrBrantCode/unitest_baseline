"""
QUESTION:
Construct a Python function named `reposition_zeros` that repositions all instances of the integer zero to the terminal position of the specified array, while preserving the sequential arrangement of the non-zero constituents. The function should handle arrays embedded within arrays, arrays with multiple data types, and arrays of any depth. The function should not utilize any pre-existing Python functions or libraries to directly address the problem and should handle cases where there are no zeros in the array, returning the original array in this case.
"""

def reposition_zeros(arr):
    if isinstance(arr, int): 
        return arr
    else:
        new_arr = []
        zeros = 0
        for item in arr:
            if isinstance(item, list):
                new_arr.append(reposition_zeros(item))
            else:
                if item == 0:
                    zeros += 1
                else:
                    new_arr.append(item)

        new_arr.extend([0]*zeros)
        return new_arr