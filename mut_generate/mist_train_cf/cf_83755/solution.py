"""
QUESTION:
Write a function `reverse_string(s, k)` that takes a string `s` and an integer `k` as input, reverses the string, and then reverses each block of `k` characters. If `k` is greater than or equal to the length of `s`, return the reversed string. If `k` is less than or equal to 0, return the original string. The function should have an optimal time complexity and handle edge cases.
"""

def reverse_string(s, k):
    if k > len(s) or k == len(s):
        return s[::-1]

    if k <= 0:
        return s

    s = list(s[::-1])
    for i in range(0, len(s), k):
        s[i:i + k] = reversed(s[i:i + k])
    
    return ''.join(s)