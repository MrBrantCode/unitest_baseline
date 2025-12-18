"""
QUESTION:
Write a function `character_prefixes_count` that takes a string `str` as input and returns a list of pairs. Each pair contains a prefix of the input string and the total count of characters in all prefixes up to that point. The prefixes should be in order from shortest to longest. The total count for each prefix is the sum of the lengths of all prefixes up to that point.
"""

def character_prefixes_count(s):
    """
    Returns a list of pairs, where each pair contains a prefix of the input string 
    and the total count of characters in all prefixes up to that point.

    Args:
    s (str): The input string.

    Returns:
    list: A list of pairs, where each pair contains a prefix and its corresponding total character count.
    """
    results = []
    prefix = ""
    total_count = 0
    for c in s:
        prefix += c
        total_count += len(prefix)
        results.append((prefix, total_count))
    return results