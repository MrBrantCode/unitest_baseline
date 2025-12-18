"""
QUESTION:
Design a function named `levenshtein_distance` that calculates the minimum number of single-character operations (insertions, deletions, and substitutions) necessary to transform one alphanumeric string into another. The function should take two strings `s1` and `s2` as input, consider both lower and upper case letters, and ensure the resulting distance is case-insensitive. The strings can be of arbitrary length between 10 and 20 characters.
"""

def levenshtein_distance(s1, s2):
    """
    Calculate the minimum number of single-character operations (insertions, deletions, and substitutions) 
    necessary to transform one alphanumeric string into another in a case-insensitive manner.

    Args:
    s1 (str): The first alphanumeric string.
    s2 (str): The second alphanumeric string.

    Returns:
    int: The Levenshtein distance between s1 and s2.
    """
    s1, s2 = s1.lower(), s2.lower()
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]