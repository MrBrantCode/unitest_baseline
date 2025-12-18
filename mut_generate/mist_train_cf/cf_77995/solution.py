"""
QUESTION:
Create a function called rearrange_tuple that takes a tuple of integers as input and returns a tuple with the elements rearranged to have all even numbers first, followed by all odd numbers, both in ascending order.
"""

def rearrange_tuple(tupl):
    """
    This function takes a tuple of integers as input, 
    and returns a tuple with the elements rearranged to have 
    all even numbers first, followed by all odd numbers, 
    both in ascending order.
    
    Parameters:
    tupl (tuple): A tuple of integers.
    
    Returns:
    tuple: A tuple with the elements rearranged.
    """
    # Separate evens and odds into two lists
    evens = [n for n in tupl if n%2 == 0]
    odds = [n for n in tupl if n%2 != 0]

    # Sort both lists in ascending order
    evens = sorted(evens)
    odds = sorted(odds)

    # Combine the sorted lists
    return tuple(evens + odds)