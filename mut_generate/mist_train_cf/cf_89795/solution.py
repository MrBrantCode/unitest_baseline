"""
QUESTION:
Create a function called `filter_array` that takes an array of mixed data types as input and returns a new array containing only the strings (case-sensitive and excluding those that start with a capital letter) and floating-point numbers, with no duplicates and in the original order. The function must have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array.
"""

def filter_array(arr):
    result = []
    seen = set()

    for element in arr:
        if type(element) == str and element.islower() and element not in seen:
            result.append(element)
            seen.add(element)
        elif type(element) == float and element not in seen:
            result.append(element)
            seen.add(element)

    return result