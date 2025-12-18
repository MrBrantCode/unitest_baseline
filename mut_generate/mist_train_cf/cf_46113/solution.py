"""
QUESTION:
Rearrange a given string of mixed uppercase and lowercase letters into a new string where the first half contains only the uppercase letters and the second half contains only the lowercase letters. The letters in both halves should be in sorted order. Implement a function `rearrange_mixed_string(s)` that takes a string `s` as input and returns the rearranged string. The length of the string is even.
"""

def rearrange_mixed_string(s):
    uppercase = sorted([c for c in s if c.isupper()])
    lowercase = sorted([c for c in s if c.islower()])
    return "".join(uppercase + lowercase)