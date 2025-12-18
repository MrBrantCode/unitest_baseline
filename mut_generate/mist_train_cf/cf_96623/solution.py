"""
QUESTION:
Create a function `calculate_most_frequent_character` that takes an input string and returns the most frequent alphabetic character in the string, ignoring punctuation and considering both uppercase and lowercase characters as the same. If there are multiple characters with the same highest frequency, return any one of them. If the input string is empty or contains no alphabetic characters, return `None`.
"""

import re
from collections import Counter

def calculate_most_frequent_character(input_string):
    # Remove punctuation and convert to lowercase
    input_string = re.sub(r'[^\w\s]', '', input_string).lower()
    
    # Count the occurrences of each character
    character_counts = Counter(input_string)
    
    # Find the most frequent character(s)
    most_frequent_characters = character_counts.most_common(1)
    
    return most_frequent_characters[0][0] if most_frequent_characters else None