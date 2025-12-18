"""
QUESTION:
Create a function `intersect_odd` that takes two lists of integers as input and returns a set of odd integers that appear in both lists along with their count. The function should achieve an optimal time and space complexity.
"""

def intersect_odd(list1, list2):
    """
    This function takes two lists of integers as input and returns a set of odd integers 
    that appear in both lists along with their count.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        set: A set of odd integers that appear in both lists.
    """
    return set(filter(lambda x: x % 2 == 1, list1)) & set(filter(lambda x: x % 2 == 1, list2))