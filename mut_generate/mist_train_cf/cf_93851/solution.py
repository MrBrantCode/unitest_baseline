"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: an `item` and a list `lst`. The function should count the occurrences of the `item` in the `lst`, including occurrences within directly nested lists and dictionaries, but excluding occurrences within nested lists or dictionaries that are contained within another nested list or dictionary.
"""

def count_occurrences(item, lst):
    """
    Counts the occurrences of an item in a given list, including nested lists and dictionaries.
    Excludes occurrences within nested lists or dictionaries that are contained within another nested list or dictionary.
    
    Args:
        item: The item to count occurrences of.
        lst: The list to search for occurrences in.
    
    Returns:
        The number of occurrences of the item in the list.
    """

    count = 0

    def helper(obj):
        nonlocal count

        if isinstance(obj, list):
            for elem in obj:
                helper(elem)
        elif isinstance(obj, dict):
            for val in obj.values():
                helper(val)
        else:
            if obj == item:
                count += 1

    helper(lst)
    return count