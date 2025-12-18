"""
QUESTION:
Write a function `reverse_transform(s)` that takes a string `s` as input and returns a string where alphabetic characters are reversed in order and their case is swapped (i.e., upper case becomes lower case and vice versa), while non-alphabetic characters remain in their original positions and are not included in the reversal.
"""

def reverse_transform(s):
    alpha_list = [c for c in s if c.isalpha()]
    alpha_list.reverse()
    result = ""
    j = 0
    for i in range(len(s)):
        if s[i].isalpha():
            result += alpha_list[j].swapcase()
            j += 1
        else:
            result += s[i]
    return result