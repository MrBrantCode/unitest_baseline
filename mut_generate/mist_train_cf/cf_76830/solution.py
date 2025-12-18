"""
QUESTION:
Write a function `sum_lower(s)` that calculates the sum of ASCII values of lowercase consonants at odd positions in the input string `s`. The function should iterate over the string at every other character starting from the second character, check if the character is a lowercase consonant (i.e., a letter between 'a' and 'z' and not a vowel), and add its ASCII value to the total sum. Return the total sum.
"""

def sum_lower(s):
    total_sum = 0
    for i in range(1, len(s), 2):
        c = s[i]
        if 'a' <= c <= 'z' and c not in "aeiou":
            total_sum += ord(c)
    return total_sum