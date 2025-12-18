"""
QUESTION:
Create a function named `process_line` that takes a line of text and a dictionary of word counts as input. The function should extract words from the line, excluding those that contain special characters or numbers, convert the words to lowercase, and update the word count dictionary. Exclude common words such as "the", "and", "is", etc. from the word count. The function should return the updated word count dictionary.

The function should work with a list of common words that can be provided as an additional input. The function should also return the words and their respective frequencies in descending order.
"""

import re
from collections import Counter

def process_line(line, word_counts, common_words):
    """
    Process a line of text and update the word count dictionary.

    Args:
    line (str): The line of text to process.
    word_counts (Counter): The dictionary to store word counts.
    common_words (list): A list of common words to exclude from the count.

    Returns:
    Counter: The updated word count dictionary.
    """
    words = re.findall(r'\b[A-Za-z]+\b', line)  # Extract words using regular expression
    words = [word.lower() for word in words]  # Convert words to lowercase
    words = [word for word in words if word not in common_words]  # Exclude common words
    word_counts.update(words)  # Update word count
    return word_counts

# Example usage:
common_words = ['the', 'and', 'is']  # Add more common words as needed
word_counts = Counter()
word_counts = process_line("This is a test line with common words.", word_counts, common_words)
print(word_counts.most_common())