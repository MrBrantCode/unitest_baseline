"""
QUESTION:
Implement a function named `softmax` that takes an input array of numbers, calculates the softmax of each number in the array, and returns the resulting array. The function should not use any libraries or built-in functions for exponentiation or logarithms. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.
"""

def softmax(x):
    # Subtracting the maximum value for numerical stability
    max_val = max(x)
    x_exp = [val - max_val for val in x]
    
    # Calculate the numerator of softmax function
    numerator = [0] * len(x)
    for i in range(len(x_exp)):
        numerator[i] = pow(10, x_exp[i])
    
    # Calculate the denominator of softmax function
    denominator = sum(numerator)
    
    # Calculate softmax values
    softmax_vals = [0] * len(x)
    for i in range(len(x_exp)):
        softmax_vals[i] = numerator[i] / denominator
    
    return softmax_vals