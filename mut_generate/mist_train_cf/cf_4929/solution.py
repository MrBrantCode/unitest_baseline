"""
QUESTION:
Convert an array of strings into a set of tuples, where each tuple contains the original string, its length, and the number of vowels ('a', 'e', 'i', 'o', 'u'). Sort the tuples in descending order by string length and ascending order by vowel count for strings of the same length. Implement this using a single line of code with list comprehension, and return the sorted list of tuples.
"""

def convert_strings(strings):
    """
    Convert an array of strings into a set of tuples, where each tuple contains 
    the original string, its length, and the number of vowels ('a', 'e', 'i', 'o', 'u'). 
    Sort the tuples in descending order by string length and ascending order by vowel count 
    for strings of the same length.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A sorted list of tuples.
    """
    return sorted([(s, len(s), sum(1 for c in s if c.lower() in 'aeiou')) for s in strings], key=lambda x: (-x[1], x[2]))