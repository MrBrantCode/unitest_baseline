"""
QUESTION:
Write a function called `add_complex_numbers` that takes two complex numbers as input and returns their sum. Each complex number is represented as a pair of real and imaginary parts. The function should not use any built-in complex number data types or arithmetic operations. The input complex numbers can be represented as tuples or objects with 'real' and 'imaginary' attributes.
"""

def add_complex_numbers(z1, z2):
    """
    This function adds two complex numbers and returns their sum.
    
    Args:
        z1 (tuple): The first complex number as a tuple of real and imaginary parts.
        z2 (tuple): The second complex number as a tuple of real and imaginary parts.
        
    Returns:
        tuple: The sum of the two complex numbers as a tuple of real and imaginary parts.
    """
    real_sum = z1[0] + z2[0]
    imag_sum = z1[1] + z2[1]
    return (real_sum, imag_sum)