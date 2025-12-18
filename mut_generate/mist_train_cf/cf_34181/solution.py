"""
QUESTION:
Create a function `top_n_words(text: str, n: int) -> List[str]` that takes a string `text` and an integer `n`, and returns a list of the top `n` most frequent words in the text, ignoring case, and breaking ties with lexicographical order.
"""

from typing import List
import re
from collections import Counter

def top_n_words(text: str, n: int) -> List[str]:
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words and convert to lowercase
    word_counts = Counter(words)  # Count the frequency of each word
    top_n = [word for word, _ in word_counts.most_common(n)]  # Get the top n most frequent words
    return sorted(top_n)  # Sort the words in lexicographical order