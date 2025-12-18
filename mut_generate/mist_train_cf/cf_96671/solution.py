"""
QUESTION:
Create a function `get_first_n_elements` that takes an array `arr` and an integer `n` as input and returns a new array containing the first `n` elements of `arr`. Implement the function without using any built-in Python functions or methods like slice or append. The function should have a time complexity of O(n) and should not use any additional data structures or variables apart from the input array and the variable used to store the first `n` elements.
"""

def get_first_n_elements(arr, n):
    result = []
    for i in range(n):
        if i >= len(arr):
            break
        result += [arr[i]]
    return result