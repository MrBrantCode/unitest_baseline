"""
QUESTION:
Write a function named `max_intersect_characters` that takes two strings as input and returns the maximum possible count of distinct intersecting characters contained within both strings.
"""

def max_intersect_characters(string1, string2):
    """
    This function calculates the maximum possible count of distinct intersecting characters contained within two strings.

    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.

    Returns:
        int: The maximum count of distinct intersecting characters.
    """
    # Convert both strings into sets of characters to eliminate duplicates
    set1 = set(string1)
    set2 = set(string2)

    # Find the intersection of both sets, which gives us unique characters present in both strings
    intersection = set1 & set2

    # The maximum count of distinct intersecting characters is the length of the intersection set
    return len(intersection)