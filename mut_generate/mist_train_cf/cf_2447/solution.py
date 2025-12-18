"""
QUESTION:
Write a function `find_most_common_words` that finds the most common words in a given string. The function should exclude common stop words such as "the", "a", "an", "and", etc., handle cases where words are separated by punctuation marks or special characters, and ignore words shorter than three characters. It should return a list of the top five most common words along with their frequency counts in descending order. The function should be efficient and handle large input strings.
"""

import re
from collections import Counter

def find_most_common_words(text):
    # Define common stop words to exclude
    stop_words = {"the", "a", "an", "and", "etc"}

    # Use regex to split the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Filter out stop words and short words
    filtered_words = [word for word in words if word not in stop_words and len(word) >= 3]

    # Count the frequency of each word
    word_counts = Counter(filtered_words)

    # Sort the words by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top five most common words
    return sorted_words[:5]