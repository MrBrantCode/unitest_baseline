"""
QUESTION:
Create a function named `custom_mix_strings` that takes two strings `s1` and `s2` as input and returns a string. The function should alternate between taking alphabetic characters from `s1` and `s2` (ignoring case sensitivity and non-alphabetic characters), and then reverse the resulting string.
"""

def custom_mix_strings(s1: str, s2: str) -> str:
    i = 0
    j = 0
    s = ""
    while (i < len(s1) or j < len(s2)) and (i < len(s1) or j < len(s2)):
        if i < len(s1):
            while i < len(s1) and not s1[i].isalpha():
                i += 1
            if i < len(s1):
                s += s1[i].lower()
                i += 1
        if j < len(s2):
            while j < len(s2) and not s2[j].isalpha():
                j += 1
            if j < len(s2):
                s += s2[j].lower()
                j += 1
    return s[::-1]