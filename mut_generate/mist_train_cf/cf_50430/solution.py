"""
QUESTION:
Write a function called `wrap_with_backticks` that takes a string `text` as input, where a certain word or phrase is selected (surrounded by some indicator). The function should return the input string with the selected word or phrase wrapped in backticks, without deleting the original text.
"""

def wrap_with_backticks(text, selected_text):
    """
    This function takes a string `text` and a `selected_text` as input.
    It returns the input string with the `selected_text` wrapped in backticks.

    Args:
        text (str): The original text.
        selected_text (str): The text to be wrapped in backticks.

    Returns:
        str: The input string with the selected text wrapped in backticks.
    """

    start = text.find(selected_text)
    end = start + len(selected_text)
    return text[:start] + '`' + text[start:end] + '`' + text[end:]