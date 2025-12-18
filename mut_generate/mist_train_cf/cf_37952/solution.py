"""
QUESTION:
Write a function named `extract_and_count` that takes two parameters: `html_text` and `target_words`. The function should extract all quoted text within `<p>` tags from `html_text` and count the occurrences of each word in `target_words` within those quotes. The function should return the extracted quoted text and the word counts. The word counts should be case-insensitive.
"""

import re

def extract_and_count(html_text, target_words):
    """
    Extracts all quoted text within <p> tags from html_text and counts the occurrences of each word in target_words within those quotes.

    Args:
        html_text (str): The input HTML text.
        target_words (list): A list of target words to count.

    Returns:
        tuple: A tuple containing the extracted quoted text and the word counts.
    """
    quoted_text = re.findall(r"<p>(.*?)<\/p>", html_text)
    word_counts = {word: 0 for word in target_words}

    for quote in quoted_text:
        for word in target_words:
            word_counts[word] += quote.lower().count(word)

    return quoted_text, word_counts