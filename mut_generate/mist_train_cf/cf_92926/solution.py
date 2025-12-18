"""
QUESTION:
Write a function named `filter_unwanted_words` that takes two parameters: a string `paragraph` and a list of strings `unwanted_words`. The function should return a new string where all occurrences of the words in `unwanted_words` are removed from `paragraph`, ignoring case sensitivity.
"""

def filter_unwanted_words(paragraph, unwanted_words):
    # Convert the paragraph to lowercase
    lowercase_paragraph = paragraph.lower()

    # Split the lowercase paragraph into tokens
    tokens = lowercase_paragraph.split()

    # Create a filtered list of tokens
    filtered_tokens = [token for token in tokens if token not in [word.lower() for word in unwanted_words]]

    # Reconstruct the filtered paragraph
    filtered_paragraph = " ".join(filtered_tokens)

    return filtered_paragraph