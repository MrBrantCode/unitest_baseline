"""
QUESTION:
Construct a function named `check_arrays` that takes two arrays `array1` and `array2` as input and returns `False` if no element in `array1` is present in `array2`, otherwise returns `True`.
"""

def check_arrays(array1, array2):
    for i in array1:
        if i in array2:
            return True
    return False