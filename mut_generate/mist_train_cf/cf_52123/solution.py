"""
QUESTION:
Create a function `vowel_count(s)` that takes a string `s` as input and returns a dictionary containing the unique vowels in the string and their corresponding occurrence count. The function should be case-insensitive and only consider the standard English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

def vowel_count(s):
    vowels = "aeiou"
    s = s.lower()
    result = {}
    for letter in s:
        if letter in vowels:
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
    return result