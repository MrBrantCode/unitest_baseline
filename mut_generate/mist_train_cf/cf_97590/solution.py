"""
QUESTION:
Create a function called `generate_story` that takes a list of strings representing bulleted text and returns a string in the format of a story. The story format is as follows: the first two bulleted points should be combined with "and" in between, followed by a period. The next two bulleted points should be combined with "and" in between and preceded by "To achieve his goal, ". The last two bulleted points should be combined with "his hard work paid off when" and "at Google." in between. Note that the input list should contain exactly six bulleted points.
"""

def generate_story(text):
    """
    Generate a story from a list of bulleted text.
    
    Args:
        text (list): A list of strings representing bulleted text.
        
    Returns:
        str: A string in the format of a story.
    """
    return text[0] + ", and " + text[1] + ". To achieve his goal, " + text[2] + " and " + text[3] + ". " + text[4] + " his hard work paid off when " + text[5] + " at Google."