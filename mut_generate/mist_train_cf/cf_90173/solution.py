"""
QUESTION:
Write a function `flatten_array` that takes a two-dimensional array as input and returns a one-dimensional array of integers. The function should exclude any element that is a negative number and is divisible by 3, as well as any element that is a string or a floating-point number. The input array can contain sublists of varying lengths, strings, and numbers.
"""

def flatten_array(arr):
    flattened = []
    for sublist in arr:
        if isinstance(sublist, list):
            for item in sublist:
                if isinstance(item, int) and item >= 0 and item % 3 != 0:
                    flattened.append(item)
        elif isinstance(sublist, int) and sublist >= 0 and sublist % 3 != 0:
            flattened.append(sublist)
    return flattened