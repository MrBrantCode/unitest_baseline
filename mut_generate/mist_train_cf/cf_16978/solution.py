"""
QUESTION:
Write a function called `concatenate_strings` that takes two strings `str1` and `str2` as input and returns a new string that is the concatenation of `str1` and `str2`. The function should not use the "+" operator or any built-in string manipulation functions. The function should have a time complexity of O(n + m) and a space complexity of O(n + m), where n and m are the lengths of `str1` and `str2` respectively.
"""

def concatenate_strings(str1, str2):
    n = len(str1)
    m = len(str2)
    result = [''] * (n + m)
    for i in range(n):
        result[i] = str1[i]
    for i in range(m):
        result[n + i] = str2[i]
    return ''.join(result)