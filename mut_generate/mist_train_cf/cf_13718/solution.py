"""
QUESTION:
Create a function `filter_unwanted_words(paragraph, unwanted_words)` that filters out unwanted words from a given paragraph of text while ignoring case sensitivity. The function should take two parameters: `paragraph`, the input text, and `unwanted_words`, a list of words to be removed. It should return the filtered paragraph as a string. The comparison between words should be case-insensitive, but the original case of the words in the paragraph should be preserved in the output.
"""

def filter_unwanted_words(paragraph, unwanted_words):
    # Convert the unwanted words to lowercase
    unwanted_words = [word.lower() for word in unwanted_words]

    # Split the paragraph into tokens
    tokens = paragraph.split()

    # Create a filtered list of tokens
    filtered_tokens = [token for token in tokens if token.lower() not in unwanted_words]

    # Reconstruct the filtered paragraph
    filtered_paragraph = " ".join(filtered_tokens)

    return filtered_paragraph