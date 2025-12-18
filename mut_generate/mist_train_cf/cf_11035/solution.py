"""
QUESTION:
Create a function called `flatten_array` that takes an array of arbitrarily nested arrays as input. The function should return a one-dimensional array containing all non-empty elements from the input array, ignoring any empty arrays or arrays that only contain empty arrays. The input array can contain a mixture of integers and strings.
"""

def flatten_array(arr):
    result = []
    for element in arr:
        if isinstance(element, list):
            if element and any(isinstance(e, list) for e in element):
                result.extend(flatten_array(element))
            elif element:
                result.extend(element)
        else:
            result.append(element)
    return result