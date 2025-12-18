"""
QUESTION:
Create a function named `check_arrays` that takes two arrays as input, `array1` and `array2`, and returns `False` only if none of the elements in `array2` are found in `array1`. The function should return `True` as soon as it finds an element in `array2` that exists in `array1`.
"""

def entrance(array1, array2):
    for i in array2:
        if i in array1:
            return True
    return False