"""
QUESTION:
Design a function `reverse_string(str)` that takes a string as input and returns the reversed string, ignoring the punctuation marks present. The function should only reverse the alphanumeric characters and maintain the relative positions of special characters.
"""

def reverse_string(s):
    s = list(s)

    # Initialize left and right pointers
    l = 0
    r = len(s) - 1

    while l < r:
        # Ignore special characters
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        # Swap characters
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    return ''.join(s)