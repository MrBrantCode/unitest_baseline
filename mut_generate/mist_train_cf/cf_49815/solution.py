"""
QUESTION:
Write a function `sort_complex_numbers` that takes a list of complex numbers as input and returns the sorted list in ascending order based on the recurrence rate of their real components. If multiple complex numbers have the same recurrence rate, they should be sorted based on their real part value.
"""

def sort_complex_numbers(sequence):
    """
    Sorts a list of complex numbers based on the recurrence rate of their real components.
    If multiple complex numbers have the same recurrence rate, they are sorted based on their real part value.

    Args:
        sequence (list): A list of complex numbers.

    Returns:
        list: The sorted list of complex numbers.
    """
    # list of real values
    real_values = [x.real for x in sequence]

    # A dictionary with real parts as keys and their frequencies as values
    real_frequencies = {x:real_values.count(x) for x in real_values}

    # Sorting the sequence based on real parts frequencies, then the real part itself
    sequence.sort(key=lambda x: (real_frequencies[x.real], x.real))

    return sequence