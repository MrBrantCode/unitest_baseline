"""
QUESTION:
Create a function `delete_empty_elements(arr)` that takes an array of strings as input and returns a new array with all empty strings removed. The function should not use built-in array manipulation methods such as `filter`, `reduce`, or `map` and should have a time complexity of O(n), where n is the length of the input array.
"""

def delete_empty_elements(arr):
    result = []
    for element in arr:
        if element != "":
            result.append(element)
    return result