"""
QUESTION:
Create a function `create_tag_cloud(paragraph, excluded_words=[])` that generates a tag cloud from a given paragraph. The function should split the paragraph into individual words, remove punctuation, and convert all words to lowercase. It should also exclude any common words specified in the `excluded_words` list. The function should then count the frequency of each word, sort them in descending order based on their frequency count, and display the tag cloud with the frequency count.
"""

import re
from collections import Counter

def create_tag_cloud(paragraph, excluded_words=[]):
    words = re.findall(r'\w+', paragraph.lower())
    words = [word for word in words if word not in excluded_words]
    word_count = Counter(words)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words