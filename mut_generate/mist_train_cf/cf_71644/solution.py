"""
QUESTION:
Write a function `highest_positive_integer` that accepts a list of elements, including integers, floats, and non-numeric values. The function should return the highest positive integer in the list, ignoring non-integer and non-numeric values. The function should handle potential errors and exceptions, including non-numeric inputs and type errors. The function should also handle decimal numbers by considering only their integer part.
"""

def highest_positive_integer(arr):
    max_int = None
    for item in arr:
        try:
            if isinstance(item, (int, float)):
                if isinstance(item, float):
                    item = int(item)
                if item > 0 and (max_int is None or item > max_int):
                    max_int = item
            else:
                print('"{}" is not an integer or decimal number and will be ignored.'.format(item))
        except TypeError as e:
            print('An error occurred: {}'.format(e))

    return max_int