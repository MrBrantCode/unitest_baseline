"""
QUESTION:
Create a function called `flatten_array` that takes a single argument `arr`, which is an array of arbitrarily nested arrays. The function should recursively flatten the array, handling cases where the input array contains a mixture of integers and strings. The function should ignore any empty arrays or arrays that only contain empty arrays.
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