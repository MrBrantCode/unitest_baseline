"""
QUESTION:
Create a function named `count_consonant_vowel_words` that takes one string argument, `sentence`. The function should return the count of words in the sentence that start with a consonant, end with a vowel, and have a length of 10 characters or less. Vowels are considered as 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase) and consonants are the rest of the alphabets. The function should ignore the case and non-alphabet characters.
"""

import re

def count_consonant_vowel_words(sentence):
    count = 0
    words = sentence.split()
    for word in words:
        if re.match(r'^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ].*[aeiouAEIOU]$', word) and len(word) <= 10:
            count += 1
    return count