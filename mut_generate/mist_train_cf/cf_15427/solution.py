"""
QUESTION:
Create a function named `reverse_only_alphanumeric`. The function should take a string as input, reverse it character by character, and return the reversed string. However, the function must ignore any non-alphanumeric characters (such as punctuation or special characters) when reversing the string. The reversed string should also maintain the same capitalization as the original string.
"""

def reverse_only_alphanumeric(s):
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return ''.join(s)