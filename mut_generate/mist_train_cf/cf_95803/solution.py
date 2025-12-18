"""
QUESTION:
Create a function named `check_list` that takes a list of integers as input and returns `True` if all elements in the list are unique, in ascending order, and are even numbers. If the conditions are met, also return the total count of unique elements and the sum of all elements in the list as a tuple `(count, sum)`, otherwise return `None`. The time complexity of the function should be less than O(n^2).
"""

def entrance(lst):
    """
    Check if all elements in a list are unique, in ascending order, and are even numbers.
    If the conditions are met, return the total count of unique elements and the sum of all elements as a tuple (count, sum), otherwise return None.

    Args:
        lst (list): A list of integers.

    Returns:
        tuple or None: A tuple containing the count of unique elements and the sum of all elements if the list meets the conditions, otherwise None.
    """

    # Check if all elements are unique and in ascending order
    if lst == sorted(set(lst)):

        # Check if all elements are even numbers
        if all(num % 2 == 0 for num in lst):
            return len(lst), sum(lst)
    
    return None