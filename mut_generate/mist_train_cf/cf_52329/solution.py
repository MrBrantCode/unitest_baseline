"""
QUESTION:
Given a string of comma-separated negative integers, write a function `remove_smallest(s)` that returns a new string with the smallest and second smallest numbers removed (if they are distinct, or just one occurrence if they are equal) and the sum of all the negative integers before removal. The function should handle edge cases properly and keep the original comma separators intact.
"""

def remove_smallest(s):
    """
    This function takes a string of comma-separated negative integers, 
    removes the smallest and second smallest numbers, and returns 
    the new string along with the sum of all the negative integers before removal.

    Args:
        s (str): A string of comma-separated negative integers.

    Returns:
        tuple: A tuple containing the new string and the sum of negative integers.
    """
    if not s:
        return '', None  # Handle the edge case of an empty string
    numbers = list(map(int, s.split(',')))
    total = sum(numbers)
    smallest = min(numbers)
    numbers.remove(smallest)
    if numbers:
        second_smallest = min(numbers)
        numbers.remove(second_smallest)
    else:
        second_smallest = None
    new_s = ','.join(map(str, numbers))
    return new_s, total