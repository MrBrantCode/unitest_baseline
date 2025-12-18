"""
QUESTION:
Create a function named `keyword_filter` that takes two parameters: a string `text` and a dictionary `keyword_dict`. The function should replace each occurrence of a keyword from `keyword_dict` in `text` with its corresponding replacement and return the updated text along with the total number of replaced keywords.
"""

def keyword_filter(text, keyword_dict):
    """
    This function filters out keywords from a given text and replaces them with their corresponding values.

    Args:
    text (str): The input text to be filtered.
    keyword_dict (dict): A dictionary containing keywords as keys and their replacements as values.

    Returns:
    tuple: A tuple containing the updated text with replaced keywords and the total count of replaced keywords.
    """
    # Initialize count of keyword occurrences
    total_keyword_occurrences = 0

    # Iterate over each keyword and its replacement
    for keyword, replacement in keyword_dict.items():
        # Count keyword occurrences in text
        keyword_occurrences = text.count(keyword)

        # Update total count
        total_keyword_occurrences += keyword_occurrences

        # Replace keyword with its replacement in text
        text = text.replace(keyword, replacement)

    # Return updated text and total count of keyword occurrences
    return text, total_keyword_occurrences