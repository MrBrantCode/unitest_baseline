"""
QUESTION:
Create a function named softmax that implements the softmax activation function in Python. The function should take an array of numbers as input and return an array of the same length with the softmax probabilities. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array. The implementation should not use any libraries, built-in functions for exponentiation or logarithms, or control flow statements (such as if, for, while, etc.).
"""

def softmax(arr):
    # Find the maximum value in the array
    max_val = max(arr)

    # Subtract the maximum value from each element to avoid overflow
    shifted_arr = [val - max_val for val in arr]

    # Exponentiate each element
    exp_arr = [2**val for val in shifted_arr]

    # Sum all the exponentiated values
    sum_exp = sum(exp_arr)

    # Divide each exponentiated value by the sum
    softmax_arr = [val / sum_exp for val in exp_arr]

    return softmax_arr