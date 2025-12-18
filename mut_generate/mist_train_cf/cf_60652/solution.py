"""
QUESTION:
Create a function `custom_multiply` that takes two distinct rational integers `num_1` and `num_2` as input parameters and returns the result of their manual multiplication operation without using the built-in multiplication operator. The function should correctly handle both positive and negative numbers.
"""

def custom_multiply(num_1, num_2):
    # Determine if result is positive or negative
    result_sign = -1 if (num_1 < 0) ^ (num_2 < 0) else 1
    
    # Conduct multiplication operation as repeated addition
    result = 0
    for i in range(abs(num_2)):
        result += abs(num_1)
    return result_sign * result