"""
QUESTION:
Implement a function named `reduce` that takes another function `func` and an array `array` as input, and returns the result of applying the `func` to all elements in the `array` from left to right, without using any built-in functions. The `reduce` function should use a loop to iterate over the array, and it should not use the `min()` function or any other built-in functions.
"""

def reduce(func, array):
    # Initialize the initial value as the first element of the array
    result = array[0]
    
    # Iterate over the remaining elements in the array
    for i in range(1, len(array)):
        # Apply the reduce function to the current result and the current element
        result = func(result, array[i])
    
    # Return the final result
    return result