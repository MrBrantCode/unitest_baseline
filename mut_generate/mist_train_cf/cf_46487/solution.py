"""
QUESTION:
Write a Python function `sort_complex_numbers` that takes a list of complex numbers as input and returns two lists. The first list is sorted in descending order based on the magnitude of the complex numbers. The second list is sorted first by the magnitude in descending order, then for those with similar magnitudes, by the real part in descending order, and finally for those with the same magnitude and real part, by the imaginary part in descending order. 

The function should use the built-in `abs` function to calculate the magnitude of the complex numbers and the `sort` method's `key` argument to customize the sort order. The `reverse=True` argument should be used to ensure the lists are sorted in descending order.
"""

def sort_complex_numbers(complex_numbers):
    """
    This function takes a list of complex numbers and returns two lists. 
    The first list is sorted in descending order based on the magnitude of the complex numbers. 
    The second list is sorted first by the magnitude in descending order, then for those with similar magnitudes, 
    by the real part in descending order, and finally for those with the same magnitude and real part, 
    by the imaginary part in descending order.

    Args:
        complex_numbers (list): A list of complex numbers.

    Returns:
        tuple: Two lists of complex numbers.
    """

    # Create a copy of the original list
    numbers_by_magnitude = complex_numbers.copy()
    numbers_by_magnitude_and_parts = complex_numbers.copy()

    # Sort by magnitude in descending order
    numbers_by_magnitude.sort(key=abs, reverse=True)

    # Sort by magnitude, real part, and imaginary part in descending order
    numbers_by_magnitude_and_parts.sort(key=lambda x: (abs(x), x.real, x.imag), reverse=True)

    return numbers_by_magnitude, numbers_by_magnitude_and_parts