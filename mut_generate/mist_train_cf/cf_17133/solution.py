"""
QUESTION:
Write a function `longest_common_prefix` that takes an array of strings `strs` as input and returns the longest common prefix string amongst all the strings in the array. The function should have a time complexity of O(n * m), where n is the number of strings in the array and m is the length of the longest string. The function should not use any built-in string comparison functions or data structures.
"""

def longest_common_prefix(strs):
    """
    This function finds the longest common prefix amongst all strings in the input array.

    Args:
        strs (list): A list of strings.

    Returns:
        str: The longest common prefix string.
    """
    prefix = ""
    if not strs:
        return prefix
    
    for i in range(len(strs[0])):
        c = strs[0][i]
        for str in strs[1:]:
            if i >= len(str) or str[i] != c:
                return prefix
        prefix += c
    
    return prefix