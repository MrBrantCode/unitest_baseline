"""
QUESTION:
Create a function called `are_scrambles` that takes two character sequence strings `s1` and `s2` as input and returns a boolean value indicating whether they are scrambled versions of each other. The function should not use any pre-established library functions or data organization systems, and it should support Unicode characters and optimize for memory usage for potentially long input strings.
"""

def count_chars(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def are_scrambles(s1, s2):
    if len(s1) != len(s2):
        return False
    char_counts1 = count_chars(s1)
    char_counts2 = count_chars(s2)
    if len(char_counts1) != len(char_counts2):
        return False
    for (char, count) in char_counts1.items():
        if char not in char_counts2 or count != char_counts2[char]:
            return False
    return True