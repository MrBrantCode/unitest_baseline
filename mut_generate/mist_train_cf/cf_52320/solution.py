"""
QUESTION:
Design a function `round_complex` that takes an array of complex numbers as input. The function should round off each complex number's real part to the nearest integer while keeping the imaginary part intact. It should handle both positive and negative numbers, and ignore non-complex number inputs.
"""

def round_complex(arr):
    """
    This function rounds off each complex number's real part to the nearest integer 
    while keeping the imaginary part intact in a given array of complex numbers.

    Args:
        arr (list): A list of complex numbers.

    Returns:
        list: A list of complex numbers with real parts rounded off.
    """
    return [round(num.real) + num.imag * 1j for num in arr if isinstance(num, complex)]