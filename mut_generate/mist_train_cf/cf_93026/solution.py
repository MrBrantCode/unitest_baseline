"""
QUESTION:
Write a function `find_longest_substring(s)` that takes a string `s` as input and returns the length of the longest substring with unique characters. The input string only contains lowercase English alphabets (a-z). If there are multiple substrings with the same longest length, return the length of the first occurring substring.
"""

def find_longest_substring(s):
    longest = ""
    current = ""

    for char in s:
        if char not in current:
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = char

    if len(current) > len(longest):
        longest = current

    return len(longest)