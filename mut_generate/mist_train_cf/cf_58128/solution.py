"""
QUESTION:
You are required to write a Python function named `string_vibrations` that returns the number of unique vibrations a string can make when played. The string is tuned to a specific set of notes, and each note corresponds to a unique vibration. The function should take a string of notes as input and return the number of unique vibrations.
"""

def string_vibrations(s):
    """
    This function calculates the number of unique vibrations a string can make when played.
    
    Parameters:
    s (str): A string of notes.
    
    Returns:
    int: The number of unique vibrations.
    """
    return len(set(s))