"""
QUESTION:
Write a function `process_visual_data` that takes in a list of integers `visual_data` representing the visual data from a HuskyLens sensor and returns a string representing the identified pattern. The function should be able to identify three patterns: "object", "face", and "other". If the visual data contains the number 1, it indicates the presence of an object, if it contains the number 2, it indicates the presence of a face, and if it contains neither, it indicates an unknown pattern.
"""

def process_visual_data(visual_data):
    """
    Process the visual data from a HuskyLens sensor and identify the pattern.

    Args:
    visual_data (list): A list of integers representing the visual data.

    Returns:
    str: A string representing the identified pattern ("object", "face", or "other").
    """
    if 1 in visual_data:
        return "object"
    elif 2 in visual_data:
        return "face"
    else:
        return "other"