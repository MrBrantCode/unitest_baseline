"""
QUESTION:
Find and replace the first instance of each string in `set1` with the corresponding string in `set2` in a given `text`. The replacement should only occur once for each pair of strings. The function should take `set1`, `set2`, and `text` as input and return the modified text. `set1` and `set2` are lists of strings and have the same length.
"""

def entrance(set1, set2, text):
    """
    Replace the first instance of each string in `set1` with the corresponding string in `set2` in a given `text`.
    
    Args:
    set1 (list): A list of strings to be replaced.
    set2 (list): A list of replacement strings.
    text (str): The input text where replacement will occur.
    
    Returns:
    str: The modified text.
    """
    for i in range(len(set1)):
        text = text.replace(set1[i], set2[i], 1)
    return text