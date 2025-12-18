"""
QUESTION:
Write a function `example_func` that takes a list as input, which may contain integers, strings, and nested sublists. For each integer in the list and its sublists, append '5' to the end of the integer (after converting it to a string). The function should handle nested sublists of any depth and avoid infinite loops. Non-integer elements should remain unchanged. Return the resulting list.
"""

def example_func(lst):
    result = []
    for element in lst:
        if type(element) == int:
            result.append(str(element) + '5')
        elif type(element) == list:
            result.append(example_func(element))   
        else:
            result.append(element)
    return result