"""
QUESTION:
Create a function named `softmax` that takes an array of numbers as input and returns an array of the same length, where each output element is the softmax of the corresponding input element. The function should not use any libraries or built-in functions for exponentiation or logarithms. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.
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