"""
QUESTION:
Create a function `extract_enclosed_words` that takes a string `text` as input. The function should return a string containing only the words enclosed between angle brackets `<>`. The input string may contain multiple lines, and each line may contain multiple words enclosed in angle brackets. The function should exclude any words not enclosed in angle brackets from the output.
"""

import re

def extract_enclosed_words(text):
    """
    This function takes a string `text` as input, extracts the words enclosed between angle brackets `<>`, 
    and returns them as a string.

    Args:
    text (str): The input string that may contain multiple lines with words enclosed in angle brackets.

    Returns:
    str: A string containing only the words enclosed between angle brackets `<>`.
    """
    # Use regex to find all occurrences of words enclosed in angle brackets
    enclosed_words = re.findall(r'<(.*?)>', text)

    # Join the extracted words into a single string separated by spaces
    extracted_text = ' '.join(enclosed_words)

    return extracted_text