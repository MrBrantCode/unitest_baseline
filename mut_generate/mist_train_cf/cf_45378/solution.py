"""
QUESTION:
Create a function called `reverse_consonants` that takes a string as input. The function should reverse the order of consonant letters in the string while keeping the vowels and special characters in place. The function should also preserve the case sensitivity of the consonant letters.
"""

def reverse_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_list = [c for c in text if c in consonants]
    output = [consonant_list.pop() if c in consonants else c for c in text]
    return ''.join(output)