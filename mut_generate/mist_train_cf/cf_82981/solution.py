"""
QUESTION:
Write a function `vowels_count(s)` that takes a string `s` as input and returns the count of vowels in the string. The function should consider 'a', 'e', 'i', 'o', 'u' as vowels, and 'y' as a vowel only when it appears at the end of the string. The function should be case-insensitive and ignore any special characters or symbols in the string.
"""

def vowels_count(s: str) -> int:
    vowels = 'aeiou'
    s = s.lower()
    count = sum(1 for char in s if char in vowels)
    # check if 'y' is a vowel in this string, add to the count if true
    if s.endswith('y'):
        count += 1
    return count