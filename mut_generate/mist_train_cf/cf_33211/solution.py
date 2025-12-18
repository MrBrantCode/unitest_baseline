"""
QUESTION:
Write a function `most_frequent_name` that takes a list of names as input and returns the most frequently occurring name. If there are multiple names with the same highest frequency, return the lexicographically smallest name among them. The input list will be provided as a series of lines, where the first line is the number of names (N) and the following N lines are the names.
"""

def most_frequent_name(names):
    """
    Returns the most frequently occurring name in the given list of names.
    If there are multiple names with the same highest frequency, returns the lexicographically smallest name among them.

    Args:
        names (list): A list of names.

    Returns:
        str: The most frequent name.
    """
    name_freq = {}
    for name in names:
        if name not in name_freq:
            name_freq[name] = 1
        else:
            name_freq[name] += 1

    name_freq = sorted(name_freq.items(), key=lambda x: (-x[1], x[0]))
    return name_freq[0][0]