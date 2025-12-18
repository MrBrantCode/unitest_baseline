"""
QUESTION:
Write a function called `longest_common_prefix` that takes an array of strings as input and returns the longest common prefix string amongst the array. The function should have a time complexity of O(n * m), where n is the number of strings in the array and m is the length of the longest string.
"""

def longest_common_prefix(strs):
    """
    Returns the longest common prefix string amongst an array of strings.

    Args:
        strs (list[str]): An array of strings.

    Returns:
        str: The longest common prefix string.
    """
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix