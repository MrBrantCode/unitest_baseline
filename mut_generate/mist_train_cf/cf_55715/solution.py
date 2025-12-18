"""
QUESTION:
Write a function `multiply_complex_numbers` that takes four lists of integers representing the digits of the real and imaginary parts of two complex numbers. Each list should be in the correct order from most significant digit to least significant digit. The function should return the product of the two complex numbers. The function should be able to handle inputs with up to 10^3 digits.
"""

def multiply_complex_numbers(a_real, a_imag, b_real, b_imag):
    """
    Multiply two complex numbers.

    Args:
    a_real (list): The real part of the first complex number as a list of digits.
    a_imag (list): The imaginary part of the first complex number as a list of digits.
    b_real (list): The real part of the second complex number as a list of digits.
    b_imag (list): The imaginary part of the second complex number as a list of digits.

    Returns:
    complex: The product of the two complex numbers.
    """
    # Convert the lists to numbers
    a_real_num = int(''.join(str(x) for x in a_real))
    a_imag_num = int(''.join(str(x) for x in a_imag))
    b_real_num = int(''.join(str(x) for x in b_real))
    b_imag_num = int(''.join(str(x) for x in b_imag))

    # Create complex numbers
    z1 = complex(a_real_num, a_imag_num)
    z2 = complex(b_real_num, b_imag_num)

    # Multiply the complex numbers
    result = z1 * z2

    return result