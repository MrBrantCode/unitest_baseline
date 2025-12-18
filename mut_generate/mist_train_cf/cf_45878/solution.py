"""
QUESTION:
Create a function called `find_frequent` that accepts an array of unique strings consisting only of alphanumeric characters. The function should return the alphanumeric character with the highest frequency across all strings, disregarding case. In cases where multiple characters have the same frequency, return the character that appears first.
"""

from collections import Counter

def find_frequent(strings):
    # Join all strings into one and convert to lowercase
    merged = ''.join(strings).lower()
    
    # Count frequency of each character
    counter = Counter(merged)
    
    # Sort characters by frequency and appearance order
    sorted_chars = sorted(counter, key=lambda x: (-counter[x], merged.index(x)))
    
    # Return the most frequent character
    return sorted_chars[0]