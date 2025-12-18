"""
QUESTION:
Write a function named `most_common_letter` that takes a string `s` as input. The function should return the letter that appears most frequently in the string, considering both uppercase and lowercase letters, numbers, and punctuations as distinct characters. If multiple letters have the same maximum frequency, the function should return the one that comes first in the alphabet. If the most frequent characters are not letters, the function should return "No alphabets".
"""

from collections import Counter

def most_common_letter(s):
    freq_count = Counter(s)
    max_count = max(freq_count.values(), default=0)
    
    candidates = [key for key, value in freq_count.items() if value == max_count and key.isalpha()]
    
    if not candidates:
        return "No alphabets"
    else:
        return min(candidates)