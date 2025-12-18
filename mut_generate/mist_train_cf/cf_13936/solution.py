"""
QUESTION:
Write a function `find_longest_substring(s)` that finds the length of the longest substring with unique characters in a given string `s`. The input string `s` contains only lowercase English alphabets (a-z). If there are multiple substrings with the same longest length, the function should return the length of the first occurring substring.
"""

def find_longest_substring(s):
    # initialize variables
    longest = ""
    current = ""

    for char in s:
        if char not in current:
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = char

    # check if the last substring is longer than the previous longest
    if len(current) > len(longest):
        longest = current

    return len(longest)