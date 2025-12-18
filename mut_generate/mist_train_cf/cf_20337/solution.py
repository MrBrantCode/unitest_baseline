"""
QUESTION:
Create a function named `multiply_list_elements` that takes a list of integers as input and returns the product of all elements in the list. The function should only use addition, subtraction, and bit shifting operations to calculate the product. The input list may contain both positive and negative integers.
"""

def multiply_list_elements(my_list):
    """
    This function calculates the product of all elements in the input list.
    
    The function uses bit manipulation to achieve multiplication.
    
    Args:
        my_list (list): A list of integers.
    
    Returns:
        int: The product of all elements in the list.
    """
    def multiply(a, b):
        result = 0
        while b > 0:
            # If b is odd, add a to result
            if b & 1:
                result += a
            # Double a and halve b
            a <<= 1
            b >>= 1
        return result

    result = 1
    for num in my_list:
        result = multiply(abs(num), result)
        
    # If the list has an odd number of negative numbers, make the result negative
    if sum(1 for x in my_list if x < 0) % 2 != 0:
        result = -result

    return result