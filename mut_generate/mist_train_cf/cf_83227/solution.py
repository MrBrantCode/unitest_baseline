"""
QUESTION:
Create a function `find_least_freq_chars` that takes a string of characters as input and returns the two least frequent letters and their corresponding frequencies. The input string may contain a mix of lowercase and uppercase alphabets, punctuation marks, and special characters. The function should ignore non-alphabetic characters, treat uppercase letters as their lowercase equivalents, and return the two letters with the lowest frequency in the string.
"""

from collections import Counter

def find_least_freq_chars(text):
    clean_text = ''.join(filter(str.isalpha, text)).lower()
    counts = Counter(clean_text)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1])
    return sorted_counts[:2]