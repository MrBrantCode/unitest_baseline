"""
QUESTION:
Design a function `find_max_sum` that takes a list as input and returns the pair of elements with the maximum sum. The list may contain integers, floating point numbers, complex numbers, nested lists, None values, boolean values, non-numeric elements, and strings convertible to numbers. 

The function must handle edge cases such as an empty list or a list with a single element, returning a suitable message in these situations. It must also handle scenarios where the list contains non-numeric elements, ignoring these and proceeding with the numeric ones. Additionally, the function must handle complex numbers, nested lists, None values, boolean values, and strings convertible to numbers. 

The function must have a time complexity better than O(n^2) to handle large lists efficiently.
"""

from numbers import Number

def find_max_sum(arr):
    values = []
    def flatten_list(lst):
        for i in lst:
            if type(i) == list:
                flatten_list(i)
            elif isinstance(i, Number):
                values.append(i)
            elif isinstance(i, bool):
                values.append(int(i))
            elif isinstance(i, str):
                try:
                    if 'j' in i:
                        values.append(complex(i))
                    else:
                        values.append(float(i.strip()))
                except:
                    continue
            elif i is None:
                continue
            else:
                continue
    flatten_list(arr)

    # Check empty list
    if len(values) < 2:
        return "Array is either empty or contains less than two numeric elements."

    n = len(values)
    sorted_vals = sorted(values, key=abs, reverse=True)
    return sorted_vals[0], sorted_vals[1]