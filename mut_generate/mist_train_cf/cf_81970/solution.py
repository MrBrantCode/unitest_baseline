"""
QUESTION:
Construct a function named cumulative_vowels that takes an array of words as input. The function should calculate the cumulative count of vowels in the given words, but only consider words that start with a vowel, end with a consonant, contain no repeated letters, and are not palindromes. The function should also exclude any words that contain non-alphabetic characters, are less than 3 characters long, or contain white spaces. The function should be case-insensitive.
"""

import re

def cumulative_vowels(array):
    vowels = "aeiouAEIOU"
    total_vowels = 0
    for word in array:
        word = re.sub(r'\s+', '', word)
        if word[0] in vowels and word[-1] not in vowels and len(set(word)) == len(word):         
            word_palindrome = word[::-1]
            if not re.match("^[a-zA-Z]*$", word) or len(word)<3 or word == word_palindrome:
                continue
            for character in word:
                if character in vowels:
                    total_vowels +=1
    return total_vowels