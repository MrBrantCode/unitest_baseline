"""
QUESTION:
Write a function `correct_count_upper(s)` that calculates the count of uppercase vowels found specifically at even indices in an input string `s`. The function should iterate over the string in steps of 2 and check if the character found at each index is an uppercase vowel. The function should return the total count of uppercase vowels at even indices.
"""

def correct_count_upper(s):
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count