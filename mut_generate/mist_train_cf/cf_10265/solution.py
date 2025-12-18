"""
QUESTION:
Find all unique occurrences of a pattern string within a text string, ignoring occurrences within a specified range of positions. Implement a function `find_occurrences(pattern, text, range_start, range_end)` that returns a list of positions where the pattern is found, considering only unique occurrences and excluding those that fall within the range defined by `range_start` and `range_end`.
"""

def find_occurrences(pattern, text, range_start, range_end):
    """
    Finds all unique occurrences of a pattern string within a text string, 
    ignoring occurrences within a specified range of positions.

    Args:
        pattern (str): The pattern to be searched in the text.
        text (str): The text where the pattern will be searched.
        range_start (int): The start of the range to be excluded.
        range_end (int): The end of the range to be excluded.

    Returns:
        list: A list of positions where the pattern is found.
    """
    occurrences = []
    start_index = 0

    while start_index < len(text):
        index = text.find(pattern, start_index)

        if index == -1:
            break

        if not range_start <= index <= range_end:
            occurrences.append(index)

        start_index = index + 1

    return occurrences