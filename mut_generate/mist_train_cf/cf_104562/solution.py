"""
QUESTION:
Write a function called `search_and_replace` that takes an array as input, replaces each numeric element with its square root rounded to the nearest whole number, and returns the modified array. Negative integers should have their absolute values calculated before taking the square root, and the negative sign should be preserved. Non-numeric elements should be left unchanged. The function should handle both integers and decimal numbers in the array.
"""

def search_and_replace(array):
    result = []
    for element in array:
        if isinstance(element, int) and element > 0:
            result.append(round(element ** 0.5))
        elif isinstance(element, int) and element < 0:
            result.append(-round(abs(element) ** 0.5))
        elif isinstance(element, float):
            result.append(round(element) ** 0.5)
        else:
            result.append(element)
    return result