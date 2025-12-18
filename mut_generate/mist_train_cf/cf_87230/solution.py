"""
QUESTION:
Write a Python function `delete_occurrences(str1: str, str2: str) -> str` that deletes all occurrences of `str2` from `str1` and returns the modified string. The input strings can contain any printable ASCII characters, and the length of `str1` can be up to 10^6. The function should have a time complexity of O(n), where n is the length of `str1`, and a space complexity of O(1). It should not use any built-in string manipulation functions or regular expressions, and should be implemented using a single pass algorithm without recursion. The function should handle edge cases efficiently, such as when `str2` is empty or when it contains special characters.
"""

def delete_occurrences(str1: str, str2: str) -> str:
    if str2 == "":
        return str1
    
    len1 = len(str1)
    len2 = len(str2)
    i = 0
    
    while i < len1:
        if str1[i:i+len2] == str2:
            str1 = str1[:i] + str1[i+len2:]
            len1 -= len2
        else:
            i += 1
    
    return str1