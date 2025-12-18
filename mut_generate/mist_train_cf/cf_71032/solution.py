"""
QUESTION:
Create a function `check_in_array` that takes a character string `str` and an array of character strings as input. The function should return a string stating whether `str` is part of the array or not. The array elements are unique and only contain strings. The input `str` is a single string.
"""

def check_in_array(str, array):
    if str in array:
        return f"{str} is part of the array"
    else:
        return f"{str} is not part of the array"