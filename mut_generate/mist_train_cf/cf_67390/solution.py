"""
QUESTION:
Write a function called `filter_consonantal_phonemes` that filters out all the terms from a given list of strings that contain fewer than two consonantal phonemes. The function should treat 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' as the consonantal phonemes.
"""

def filter_consonantal_phonemes(lst):
    """
    Filters out all the terms from a given list of strings that contain fewer than two consonantal phonemes.
    
    Parameters:
    lst (list): A list of strings.
    
    Returns:
    list: A list of strings containing two or more consonantal phonemes.
    """
    consonantal_phonemes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return [term for term in lst if sum(ch in consonantal_phonemes for ch in term) >= 2]