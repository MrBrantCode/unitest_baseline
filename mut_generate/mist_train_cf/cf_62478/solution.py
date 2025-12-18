"""
QUESTION:
Write a function `sort_complex_numbers` that sorts a list of complex numbers based on the frequency of their real parts and, in cases of equal frequency, by the frequency of their imaginary parts. The function should take a list of complex numbers as input and return the sorted list. The sorting should be in descending order of frequency.
"""

from collections import Counter

def sort_complex_numbers(lst):
    """
    Sorts a list of complex numbers based on the frequency of their real parts 
    and, in cases of equal frequency, by the frequency of their imaginary parts.
    
    Parameters:
    lst (list): A list of complex numbers.
    
    Returns:
    list: The sorted list of complex numbers.
    """
    
    # Extract the real and imaginary parts
    real_parts = [x.real for x in lst]
    imag_parts = [x.imag for x in lst]

    # Count occurrences of real and imaginary parts
    real_counts = Counter(real_parts)
    imag_counts = Counter(imag_parts)

    # Define a comparing function
    def compare_func(x):
        real_count = real_counts[x.real]
        imag_count = imag_counts[x.imag]
        return (real_count, imag_count)

    # Sort the list firstly by imaginary part counts, then by real part counts
    lst_sorted = sorted(lst, key=compare_func, reverse=True)

    return lst_sorted