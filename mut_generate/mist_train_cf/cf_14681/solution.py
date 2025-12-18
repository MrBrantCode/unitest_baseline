"""
QUESTION:
Write a function `extract_names` that extracts names from a given sentence using regex. The function should only extract names that are preceded by the word "and" and followed by the word "went". The names may be separated by commas or other characters.
"""

import re

def extract_names(sentence):
    """
    Extracts names from a given sentence using regex.
    The function only extracts names that are preceded by the word "and" and followed by the word "went".
    
    Parameters:
    sentence (str): The input sentence.
    
    Returns:
    list: A list of extracted names.
    """
    pattern = r'(?<=and\s)\b\w+\b(?=\swent)'
    names = re.findall(pattern, sentence)
    return names