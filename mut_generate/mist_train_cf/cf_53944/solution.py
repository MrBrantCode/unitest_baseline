"""
QUESTION:
Write a function `highest_frequency_chars` that takes a string as input and returns a list of characters with the highest frequency in the string, ignoring white space and punctuation. If multiple characters have the same highest frequency, they should be returned in the order they first appear in the string. The function should be case-insensitive.
"""

def highest_frequency_chars(phrase):
    phrase = phrase.lower()
    counts = {}
    max_count = 0
    for char in phrase:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
            max_count = max(max_count, counts[char])
            
    return [char for char, count in counts.items() if count == max_count]