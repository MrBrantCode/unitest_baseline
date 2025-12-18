"""
QUESTION:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:


Input: ["flower","flow","flight"]
Output: "fl"


Example 2:


Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Note:

All given inputs are in lowercase letters a-z.
"""

def find_longest_common_prefix(strs):
    """
    Finds the longest common prefix string amongst an array of strings.

    Parameters:
    strs (list of str): A list of strings for which to find the longest common prefix.

    Returns:
    str: The longest common prefix string. If there is no common prefix, returns an empty string.
    """
    if not strs:
        return ""
    
    import os
    return os.path.commonprefix(strs)