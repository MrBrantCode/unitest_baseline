"""
QUESTION:
Write a function named `generate_story` that takes a list of strings representing bulleted text as input. The function should return a string that combines the input bulleted text into a story in a specific format. The first two input strings should be combined with ", and " in between, followed by ". To achieve his goal, " and then the next two strings combined with " and " in between, followed by ". Finally, " and the last two strings combined with " and " in between. The input list should have exactly six strings.
"""

def generate_story(text):
    """
    Combines bulleted text into a story in a specific format.

    Args:
    text (list): A list of six strings representing bulleted text.

    Returns:
    str: A string that combines the input bulleted text into a story.
    """
    return text[0] + ", and " + text[1] + ". To achieve his goal, " + text[2] + " and " + text[3] + ". " + text[4] + " and " + text[5]