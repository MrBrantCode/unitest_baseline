"""
QUESTION:
Write a function `process_elements` that takes a multidimensional array as input and returns the summation of all numerical elements and the concatenation of all string-like elements. The function should handle arrays of mixed data types and recursively process nested arrays. If the array contains both numerical and string-like elements, the function should return a string that is the concatenation of the summation and the concatenation, with the summation as an integer and the concatenation as a string.
"""

def process_elements(arr):
    if not isinstance(arr, list):
        return arr
    summation = 0
    concatenation = ""
    for elem in arr:
        if isinstance(elem, list):
            result = process_elements(elem)
            if isinstance(result, int):
                summation += result
            elif isinstance(result, str):
                concatenation += result
        elif isinstance(elem, int):
            summation += elem
        elif isinstance(elem, str):
            concatenation += elem
    if concatenation == "":
        if summation == 0 and len(arr) > 0:
            return str(summation) + concatenation
        return summation 
    elif summation == 0:
        return concatenation
    return str(summation) + concatenation