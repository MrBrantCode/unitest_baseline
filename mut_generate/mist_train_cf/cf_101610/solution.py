"""
QUESTION:
Create a function named `generate_story` that takes a list of strings representing bulleted text as input. The function should return a single string representing the generated story. The generated story should be in the following format: 
"The first sentence, and the second sentence. To achieve his goal, the third sentence and the fourth sentence. Finally, the fifth sentence and the sixth sentence at Google."
"""

def generate_story(text):
    """
    This function takes a list of strings representing bulleted text as input and returns a single string representing the generated story.
    
    Args:
    text (list): A list of strings representing bulleted text.

    Returns:
    str: A single string representing the generated story.
    """
    return text[0] + ", and " + text[1] + ". To achieve his goal, " + text[2] + " and " + text[3] + ". " + text[4] + " and " + text[5] + " at Google."