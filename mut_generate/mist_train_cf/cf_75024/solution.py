"""
QUESTION:
Design a function named `check_zeros` that accepts a 2D array and returns `True` only if all elements are numerical zeroes, otherwise it should return `False`. The function must not use numpy's built-in functions to check for non-zero elements and should traverse the array manually checking each element. 

Create a 4x3 2D NumPy array with all elements as numerical zeroes without using the `np.zeros()` function.
"""

def check_zeros(array):
    for row in array:
        for elem in row:
             # If any element is nonzero, return False
             if elem != 0:
                  return False
    # If we haven't returned False yet, all elements are zero, thus return True.
    return True