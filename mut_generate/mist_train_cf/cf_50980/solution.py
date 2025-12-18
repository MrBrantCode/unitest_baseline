"""
QUESTION:
Write a function `reverseString(s)` that takes an array of characters `s` as input and reverses the string without affecting the positions of the special characters. The function should modify the input array in-place with `O(1)` extra memory. 

`1 <= s.length <= 10^5` and `s[i]` is a printable ascii character.
"""

def reverseString(s):
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return s