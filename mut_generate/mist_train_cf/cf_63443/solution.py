"""
QUESTION:
Write a function `vowels_count(s)` that takes a string `s` as input and returns the number of vowels in the string. Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' only when found at the end of the string. The function should be case-insensitive and handle special characters, numbers, blank spaces, and empty strings within the input string.
"""

def vowels_count(s):
    """Compose a function 'vowels_count', accepting a string representing
    a word as input, returning the number of vowels in the string.
    Vowels, in this case, are 'a', 'e', 'i', 'o', 'u', and 'y' ONLY when
    found at the end of the input word. Ignore case and include special
    characters, numbers, blank spaces, and empty strings within the input word.
    """
    count = 0
    if s == '':
         return count;
    s = s.lower()

    for char in s:
        if char in 'aeiou':
            count += 1
    if s[-1] == 'y':
        count += 1

    return count