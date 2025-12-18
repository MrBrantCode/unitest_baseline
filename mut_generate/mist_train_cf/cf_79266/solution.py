"""
QUESTION:
Write a function `count_substring` that takes two parameters: `text` and `substring`. The function should return the number of occurrences of the `substring` within the `text`, allowing for overlapping occurrences. The function should only count distinct sequences of characters as separate occurrences when they do not overlap.
"""

def count_substring(text, substring):
    """
    Returns the number of occurrences of the substring within the text, 
    allowing for overlapping occurrences.

    Args:
    text (str): The text to search for the substring.
    substring (str): The substring to search for.

    Returns:
    int: The number of occurrences of the substring.
    """
    count = start = 0
    while start < len(text):
        pos = text.find(substring, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count