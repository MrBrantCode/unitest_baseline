"""
QUESTION:
Create a function called `delete_empty_elements` that takes an array of strings as input, removes all empty strings from the array, and returns the updated array. The function should not use built-in array manipulation methods like `filter`, `reduce`, or `map` and should have a time complexity of O(n), where n is the length of the input array.
"""

def delete_empty_elements(arr):
    result = []
    for element in arr:
        if element != "":
            result.append(element)
    return result