"""
QUESTION:
Create a function `reverse_substring` that takes a string and an integer `n` as input. The function should reverse the substring starting from the nth character and ending at the (2*n)th character. If there are less than (2*n) characters after the nth character, reverse the substring until the end of the string. The function should return the modified string.
"""

def reverse_substring(s, n):
    if n >= len(s):
        return s

    end_index = min(n + 2 * n, len(s))
    substring = s[n:end_index]
    reversed_substring = substring[::-1]

    return s[:n] + reversed_substring + s[end_index:]