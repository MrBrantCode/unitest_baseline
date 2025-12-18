"""
QUESTION:
Create a function `can_transform` that takes two binary strings `bin_str1` and `bin_str2` as input. The function should return `True` if `bin_str1` can be transformed into `bin_str2` by flipping exactly one bit, and `False` otherwise. The function should assume that the input strings only contain '0' and '1' characters. The length of `bin_str1` and `bin_str2` must be the same, otherwise the function should return `False`.
"""

def can_transform(bin_str1, bin_str2):
    diff_count = 0
    # Check if lengths are the same
    if len(bin_str1) != len(bin_str2):
        return False
    # Check if exactly one bit differs between strings
    for i in range(len(bin_str1)):
        if bin_str1[i] != bin_str2[i]:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1