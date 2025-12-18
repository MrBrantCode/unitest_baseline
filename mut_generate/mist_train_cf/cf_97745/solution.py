"""
QUESTION:
Write a Python function `generate_story` that takes a list of strings representing bulleted text and returns a string representing a story. The function should combine the strings in the list to create a coherent story, using the following format: the first two strings should be joined with ", and ", the next two strings should be joined with " and " and preceded by "To achieve his goal, ", and the last two strings should be joined with a period after the fifth string.
"""

def generate_story(text):
    """
    Combines the strings in the list to create a coherent story.

    Args:
    text (list): A list of strings representing bulleted text.

    Returns:
    str: A string representing a story.
    """
    return text[0] + ", and " + text[1] + ". To achieve his goal, " + text[2] + " and " + text[3] + ". " + text[4] + " " + text[5] + "."