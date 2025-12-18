"""
QUESTION:
Create a function `replaceAndSort(words)` that takes an array of words as input, where each word can be at most 10 characters long and may contain uppercase letters, lowercase letters, special characters, and numbers. The function should convert all words to lowercase, ignore non-alphabet characters, replace each alphabet character with its corresponding number (a=1, b=2, ..., z=26), compute the sum of these numbers for each word, and return the array of words sorted in ascending order based on their computed sums.
"""

def replaceAndSort(words):
    return sorted((word.lower() for word in words), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word if c.isalpha()))