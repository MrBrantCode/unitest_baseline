"""
QUESTION:
Create a function named `remove_dup` that takes a string `s` as input and returns a new string with duplicate characters removed while maintaining the original order of characters. The function should have a time complexity of O(N), where N is the size of the string. You cannot use any built-in or library methods to remove duplicates from the string. Implement the solution manually.
"""

def remove_dup(s):
    exists = set()
    res = []
    for char in s:
        if char not in exists:
            exists.add(char)
            res.append(char)
    return "".join(res)