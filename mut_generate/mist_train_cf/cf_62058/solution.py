"""
QUESTION:
Write a function named `consonant_count` that takes a string `s` as input and returns the total count of consonants in the string. The function should consider both lowercase and uppercase characters and ignore numerical digits and punctuation marks.
"""

def consonant_count(s: str) -> int:
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0  
    for char in s:
        if char in consonants:
            count += 1
    return count