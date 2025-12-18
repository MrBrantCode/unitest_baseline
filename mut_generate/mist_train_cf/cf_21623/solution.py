"""
QUESTION:
Implement a function named `get_first_n_elements` that takes an array and an integer n as input and returns the first n elements from the array. The function should not use any built-in Python functions or methods such as slice or append, and should have a time complexity of O(n). The function should not use any additional data structures or variables apart from the input array and the variable used to store the first n elements.
"""

def get_first_n_elements(arr, n):
    result = []
    for i in range(n):
        if i >= len(arr):
            break
        result += [arr[i]]
    return result