"""
QUESTION:
Create a function `element_frequency` that takes a list of integers as input and returns a list of tuples, where each tuple contains an element from the list and its frequency. The list of tuples should be sorted in descending order of frequency. If two elements have the same frequency, they should be sorted in ascending order. The function should not take any other arguments.
"""

def element_frequency(lst):
    """
    Returns a list of tuples, where each tuple contains an element from the list and its frequency.
    The list of tuples is sorted in descending order of frequency. If two elements have the same frequency,
    they are sorted in ascending order.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A list of tuples containing elements and their frequencies.
    """
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    return sorted(frequency.items(), key=lambda x: (-x[1], x[0]))