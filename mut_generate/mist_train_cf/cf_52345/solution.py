"""
QUESTION:
Write a function `swap_quadruplets(s, count)` that takes a string `s` of digits and an integer `count` as input. The function should swap the first `count` quadruplets (groups of 4 consecutive digits) in the string, and return the modified string. The function should preserve the order of the remaining quadruplets that are not swapped.
"""

def entrance(s, count):
    n = 4  # quadruplets
    quadruplets = [s[i:i+n] for i in range(0, len(s), n)]
    swapped_quadruplets = quadruplets[count-1::-1] + quadruplets[count:]
    swapped = ''.join(swapped_quadruplets)
    return swapped