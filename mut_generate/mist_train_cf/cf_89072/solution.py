"""
QUESTION:
Create a function `create_tag_cloud` that takes a paragraph of text and a list of excluded words as input. The function should tokenize the paragraph into individual words, remove punctuation, and convert all words to lowercase. It should then exclude the specified common words and count the frequency of each remaining word. The function should output the words and their frequency counts in descending order of frequency.
"""

import re
from collections import Counter

def create_tag_cloud(paragraph, excluded_words=[]):
    # Tokenize the paragraph by splitting into words
    words = re.findall(r'\w+', paragraph)

    # Remove punctuation and convert to lowercase
    words = [word.lower() for word in words]

    # Exclude common words specified by the user
    words = [word for word in words if word not in excluded_words]

    # Count the frequency of each word
    word_count = Counter(words)

    # Sort the words based on frequency count in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted words with frequency count
    return sorted_words