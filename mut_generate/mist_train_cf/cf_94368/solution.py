"""
QUESTION:
Create a function `get_odd_numbers_as_strings` that takes an integer `n` as input and returns a list of string representations of odd numbers from 0 to `n` in descending order with no duplicates. The function should not take any other parameters besides `n`.
"""

def get_odd_numbers_as_strings(n):
    """
    Returns a list of string representations of odd numbers from 0 to n in descending order with no duplicates.

    Args:
        n (int): The upper limit of the range.

    Returns:
        list: A list of string representations of odd numbers.
    """
    # Create an array with odd numbers from 0 to n, convert each number to its string representation
    # and remove any duplicates
    arr = list(set(str(i) for i in range(n+1) if i % 2 != 0))
    
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    return arr