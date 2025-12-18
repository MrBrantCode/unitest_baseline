"""
QUESTION:
Write a function to determine the time complexity of an algorithm using Big O notation. The function should take as input a string representing the time complexity (e.g., 'O(n^2)', 'O(n log n)', etc.) and return a simplified string representing the time complexity in Big O notation. The function should be able to handle common time complexities such as O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), etc.
"""

def simplify_time_complexity(time_complexity_str):
    """
    Simplify a given time complexity string.

    Args:
    time_complexity_str (str): Time complexity string (e.g., 'O(n^2)', 'O(n log n)')

    Returns:
    str: Simplified time complexity string in Big O notation.
    """

    # Remove the 'O(' and ')' from the input string
    time_complexity_str = time_complexity_str.replace('O(', '').replace(')', '')

    # Remove any spaces from the input string
    time_complexity_str = time_complexity_str.replace(' ', '')

    # Check for common time complexities
    if time_complexity_str == '1':
        return 'O(1)'
    elif time_complexity_str == 'logn':
        return 'O(log n)'
    elif time_complexity_str == 'n':
        return 'O(n)'
    elif time_complexity_str == 'nlogn':
        return 'O(n log n)'
    elif time_complexity_str == 'n^2':
        return 'O(n^2)'
    elif time_complexity_str == '2^n':
        return 'O(2^n)'
    else:
        # If the time complexity is not recognized, return the original string
        return 'O(' + time_complexity_str + ')'