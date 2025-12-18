"""
QUESTION:
Design a function `reverse_string` that takes an input string `str` of length `n` containing alphanumeric characters, special characters, and punctuation marks. The function should reverse the alphanumeric characters in the string while keeping the special characters and punctuation marks in their original positions. The function must be done in-place and have a time complexity of O(n).
"""

def reverse_string(s):
    n = len(s)
    s = list(s)
    l = 0
    r = n - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    return ''.join(s)