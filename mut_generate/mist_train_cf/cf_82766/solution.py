"""
QUESTION:
Write a function called complex_operations that takes a complex number and/or real numbers as input, and returns the result of different operations on the complex number. The function should be able to handle inputs such as (31+5j), (31+5j.real), (31+5j.imag), 42, 42.real, 42.imag, complex(20+10j,5+5j), and complex(10+10j,5+5j). The function should also be able to add two complex numbers directly.
"""

def complex_operations(a, b=None):
    """
    This function performs different operations on complex numbers.
    
    Parameters:
    a (complex or int): The first complex number or real number.
    b (complex or int, optional): The second complex number or real number. Defaults to None.
    
    Returns:
    complex or int: The result of the operation.
    """

    # Check if b is provided
    if b is not None:
        # If b is provided, add a and b
        return a + b
    else:
        # If b is not provided, return a as is
        return a