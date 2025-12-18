"""
QUESTION:
Create a function `shortest_string(s1, s2, s3)` that takes three strings as input and returns the shortest string without any vowels. The function should remove vowels from each input string, compare the lengths of the resulting strings, and return the shortest one.
"""

def shortest_string(s1, s2, s3):
    def remove_vowels(s):
        return ''.join(c for c in s if c.lower() not in 'aeiou')

    s1_no_vowels = remove_vowels(s1)
    s2_no_vowels = remove_vowels(s2)
    s3_no_vowels = remove_vowels(s3)

    min_len = min(len(s1_no_vowels), len(s2_no_vowels), len(s3_no_vowels))

    if len(s1_no_vowels) == min_len:
        return s1_no_vowels
    elif len(s2_no_vowels) == min_len:
        return s2_no_vowels
    else:
        return s3_no_vowels