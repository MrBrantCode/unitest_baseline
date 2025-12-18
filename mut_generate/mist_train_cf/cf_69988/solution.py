"""
QUESTION:
Write a function `longest_common_prefix` that takes a list of strings as input and returns the longest common prefix among all strings in the list. The function should return an empty string if the input list is empty.
"""

def longest_common_prefix(strs):
    if not strs: return ""
    
    # Sort the array
    strs.sort()
    
    # The result will be characters of the smallest string.
    res = []
    
    # The smallest and the largest strings in the array.
    smallest, largest = strs[0], strs[-1]
    
    # Find the smallest length string in the array
    for i in range(len(smallest)):
        # Check if the characters match in the smallest and the largest strings.
        if smallest[i] == largest[i]:
            res.append(smallest[i])
        else:
            return "".join(res)
    return "".join(res)