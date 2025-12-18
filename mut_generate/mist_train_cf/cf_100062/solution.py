"""
QUESTION:
Generate a story from a set of bulleted text in the following format: 
The first two points should be connected with "and", then the next two points should be connected with "and" and preceded by "To achieve his goal, ". The last two points should be connected with "at Google." but the word at Google should be placed after the second last point. The function name should be generate_story.
"""

def generate_story(text):
    """
    Generate a story from a set of bulleted text.
    
    Args:
    text (list): A list of strings representing the bulleted text.
    
    Returns:
    str: The generated story.
    """
    return text[0] + ", and " + text[1] + ". To achieve his goal, " + text[2] + " and " + text[3] + ". " + text[4] + " at Google, " + text[5]