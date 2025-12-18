"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of strings as input. The function should remove duplicates from the list while preserving the original order of unique strings and return the list of unique strings. The function should also return the count of each unique string and display the top 3 most occurring strings in descending order of their counts. If multiple strings have the same count, they should be displayed in lexicographical order.
"""

from collections import Counter, OrderedDict

def remove_duplicates(strings):
    """
    Remove duplicates from a list of strings, preserving the original order of unique strings.
    Return the list of unique strings and display the top 3 most occurring strings.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of unique strings.
    """
    unique_strings = list(OrderedDict.fromkeys(strings))
    counts = Counter(strings)
    top3 = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]
    for string, count in top3:
        print(f"{string}: {count} occurrences")
    return unique_strings