"""
QUESTION:
Write a function `compare_strings(s1, s2)` that compares two input strings `s1` and `s2` lexicographically without using built-in comparison operators or functions. The function should return an integer: -1 if `s1` is lexicographically less than `s2`, 1 if `s1` is lexicographically greater than `s2`, and 0 if `s1` and `s2` are lexicographically equal. Additionally, implement a helper function `get_ascii(char)` to calculate the ASCII value of a character without using the built-in `ord()` function.
"""

def compare_strings(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1

    result = 0
    for c1, c2 in zip(s1,s2):
        if get_ascii(c1) < get_ascii(c2):
            result = -1
            break
        elif get_ascii(c1) > get_ascii(c2):
            result = 1
            break
    else:
        if len(s1) == len(s2):
            result = 0
        elif len(s1) < len(s2):
            result = -1
        else:
            result = 1

    return result


### get_ascii function
def get_ascii(char):
    return sum(bytearray(char, 'utf-8'))