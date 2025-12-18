"""
QUESTION:
Implement a method `get_summary` that takes an integer `max_length` as a parameter. The method should return a summary of the post's content by truncating the `text` field to a specified length and appending an ellipsis if the text exceeds the specified length. The summary should prioritize breaking at the end of a sentence and should not cut off words in the middle. If the text is shorter than the specified length, the entire text should be returned.
"""

def get_summary(text, max_length):
    """
    Returns a summary of the post's content by truncating the text to a specified length 
    and appending an ellipsis if the text exceeds the specified length.

    Args:
        text (str): The text to be summarized.
        max_length (int): The maximum length of the summary.

    Returns:
        str: A summary of the post's content.
    """
    if len(text) <= max_length:
        return text
    else:
        summary = text[:max_length]
        last_period = summary.rfind('.')
        if last_period != -1 and last_period > max_length - 20:
            return summary[:last_period + 1]
        else:
            return summary + '...'