"""
QUESTION:
Write a function named `remove_non_alphanumeric` that takes a string as input. The function should remove all non-alphanumeric characters from the string, convert all uppercase letters to lowercase, and sort the resulting string in reverse alphabetical order. Additionally, it should count the frequency of each letter and return the sorted string. The top three most frequent letters and their frequencies should also be printed.
"""

import re
from collections import Counter

def remove_non_alphanumeric(text):
    # Remove non-alphanumeric characters and convert uppercase letters to lowercase
    text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    
    # Sort the resulting string in reverse alphabetical order
    sorted_text = sorted(text, reverse=True)
    
    # Count the frequency of each letter
    frequency = Counter(sorted_text)
    
    # Display the top three most frequent letters and their frequencies
    top_three = frequency.most_common(3)
    
    for letter, count in top_three:
        print(f"{letter}: {count}")
    
    return sorted_text