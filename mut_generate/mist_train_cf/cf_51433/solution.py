"""
QUESTION:
Write a function called `max_consonants` that accepts a dictionary with English words as keys and their meanings as values. The function should return the key that contains the maximum quantity of consonant letters.
"""

def max_consonants(d):
    max_consonants = 0
    max_key = ""
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    for key in d:
        count = sum(1 for char in key if char in consonants)
        if count > max_consonants:
            max_consonants = count
            max_key = key
    return max_key