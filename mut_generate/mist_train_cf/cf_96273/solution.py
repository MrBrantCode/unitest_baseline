"""
QUESTION:
Write a function called `symmetric_difference` that takes two sets `set1` and `set2` as input. Each set should contain between 10 and 15 positive integers between 1 and 10000. The function should return a tuple containing the symmetric difference of the two sets and the count of distinct elements in the symmetric difference set. The function should have a time complexity of O(n), where n is the total number of elements in both sets.
"""

def symmetric_difference(set1, set2):
    """
    This function calculates the symmetric difference of two sets and returns a tuple containing the symmetric difference set and the count of distinct elements.

    Args:
        set1 (set): The first set containing between 10 and 15 positive integers between 1 and 10000.
        set2 (set): The second set containing between 10 and 15 positive integers between 1 and 10000.

    Returns:
        tuple: A tuple containing the symmetric difference set and the count of distinct elements.
    """

    # Calculate the symmetric difference of the two sets
    sym_diff = set1.symmetric_difference(set2)

    # Count the distinct elements in the symmetric difference set
    count = len(sym_diff)

    # Return the symmetric difference set and the count of distinct elements as a tuple
    return sym_diff, count