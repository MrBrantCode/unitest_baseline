"""
QUESTION:
Write a function `count_upper_vowels(s)` that calculates the number of uppercase vowels at even index positions in the input string `s`. The function should return the count of uppercase vowels. Note that index positions are zero-based, meaning the first character is at index 0.
"""

def count_upper_vowels(s):
    counter = 0
    vowels = 'AEIOU'
    for i, char in enumerate(s):
        if i % 2 == 0 and char in vowels:
            counter += 1
    return counter