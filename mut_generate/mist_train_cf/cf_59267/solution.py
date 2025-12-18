"""
QUESTION:
Create a function named `complex_vowels_count` that accepts a string of characters and returns the count of vowels in the string. The function should consider 'a', 'e', 'i', 'o', 'u', and 'y' (only when at the end of the word) as vowels, handle the inclusion of complex special characters within the word, and ignore case.
"""

def complex_vowels_count(s):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    s = s.lower()

    for char in s:
        if char in vowels:
            count += 1
        elif ord(char) in [225, 233, 237, 243, 250, 253]:  # accents in ascii
            count += 1
    return count