"""
QUESTION:
Create a function named `custom_mix_strings` that takes two strings `s1` and `s2` as input, combines them by alternating their characters starting with the longer string, and returns the mixed string in reverse order. If the strings are of equal length, simply alternate their characters. If the strings are of unequal length, alternate their characters until the end of the shorter string is reached, then append the remaining characters from the longer string. Finally, reverse the mixed string before returning it. The function should work correctly even if one or both of the input strings are empty.
"""

def custom_mix_strings(s1: str, s2: str) -> str:
    if len(s1) == len(s2):
        mixed_string = "".join([s1[i] + s2[i] for i in range(len(s1))])
    elif len(s1) > len(s2):
        mixed_string = "".join([s1[i] + s2[i] for i in range(len(s2))]) + s1[len(s2):]
    else:
        mixed_string = "".join([s2[i] + s1[i] for i in range(len(s1))]) + s2[len(s1):]
    return mixed_string[::-1]