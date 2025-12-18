"""
QUESTION:
Create a function `multiply_and_sum` that takes an array of integers as input. The function should iterate through the array, multiplying each element by its index if the element is greater than or equal to its index, and sum the results. Exclude elements that are less than their index from the calculation. Return the final sum.
"""

def multiply_and_sum(arr):
    result = 0
    for i in range(len(arr)):
        if arr[i] >= i:
            result += arr[i] * i
    return result