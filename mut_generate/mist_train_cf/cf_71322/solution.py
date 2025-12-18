"""
QUESTION:
Create a function called `check_exclusivity` that takes a string `text` as input and returns a boolean value indicating whether all alphabetical letters in the string are unique. The function should ignore non-alphabetical characters and case sensitivity.
"""

def check_exclusivity(text):
    """
    Checks if all alphabetical letters in the given text are unique, ignoring non-alphabetical characters and case sensitivity.

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if all alphabetical letters are unique, False otherwise.
    """
    return len(set(ch.lower() for ch in text if ch.isalpha())) == len([ch for ch in text if ch.isalpha()])