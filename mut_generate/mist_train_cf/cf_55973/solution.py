"""
QUESTION:
Write a function `multiply_lists` that takes two lists of complex numbers as input, where each complex number is represented as a tuple of two integers (real part, imaginary part). The function should return a tuple representing the sum of the products of all pairs of complex numbers from the two input lists. The function should not use any built-in complex number operations. The time complexity of the function should be O(n^2), where n is the length of each list.
"""

def multiply_complex(a, b): 
    """
    Helper function to multiply two complex numbers.
    
    Args:
        a (tuple): A complex number represented as a tuple of two integers (real part, imaginary part).
        b (tuple): A complex number represented as a tuple of two integers (real part, imaginary part).
    
    Returns:
        tuple: The product of two complex numbers as a tuple.
    """
    real_part = a[0]*b[0] - a[1]*b[1]
    imaginary_part = a[1]*b[0] + a[0]*b[1]
    return (real_part, imaginary_part)


def multiply_lists(first_list, second_list): 
    """
    Function to calculate the sum of the products of all pairs of complex numbers from two input lists.
    
    Args:
        first_list (list): A list of complex numbers, where each complex number is a tuple of two integers.
        second_list (list): A list of complex numbers, where each complex number is a tuple of two integers.
    
    Returns:
        tuple: The sum of the products of all pairs of complex numbers as a tuple.
    """
    result = (0, 0)
    for element in first_list: 
        for value in second_list: 
            product = multiply_complex(element, value)
            result = (result[0] + product[0], result[1] + product[1])
    return result