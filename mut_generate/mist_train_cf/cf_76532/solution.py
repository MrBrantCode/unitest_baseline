"""
QUESTION:
Design an algorithm that calculates the product of an array of complex numbers. The function, named `product_of_complex_numbers`, should take an array of complex numbers as input and return their product. If the input array contains non-complex numbers, the function should return an error message. Additionally, the function should handle potential overflows by returning a precision error message if the product exceeds the maximum limit.
"""

import numpy as np

def product_of_complex_numbers(array):
    # Check if every element is a complex number
    if not all(isinstance(i, complex) for i in array):
        return 'Error: all elements must be complex numbers' 

    result = complex(1, 0) # Start with a complex number 1
    
    for num in array:
        temp_result = result * num
        
        # If overflow, return error message
        if np.isinf(temp_result):
            return 'Error: Precision overflow'
        
        result = temp_result
        
    return result