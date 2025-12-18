"""
QUESTION:
Write a function called most_occurring_multiple_of_3 that takes a list of integers as input and returns the most frequently occurring number that is divisible by 3. If no such number exists, the function should return None. The function should not modify the input list and should handle empty input lists.
"""

from collections import Counter

def most_occurring_multiple_of_3(lst):
    """
    This function takes a list of integers as input and returns the most frequently occurring number that is divisible by 3.
    If no such number exists, the function returns None.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    int or None: The most frequently occurring number that is divisible by 3, or None if no such number exists.
    """

    # Filter the list to only include numbers divisible by 3
    divisible_by_3 = [x for x in lst if x % 3 == 0]

    # If no numbers are divisible by 3, return None
    if not divisible_by_3:
        return None

    # Use Counter to find the most occurring item
    counter = Counter(divisible_by_3)
    most_occurring = counter.most_common(1)[0][0]

    return most_occurring