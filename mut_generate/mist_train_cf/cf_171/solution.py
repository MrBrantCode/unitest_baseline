"""
QUESTION:
Write a function `extract_words` that takes two parameters: `input_str` (a string) and `letter` (a single character). The function should return a list of words from `input_str` that start with `letter` (case-sensitive) and contain at least two uppercase letters. The extracted words should be in uppercase.
"""

import re

def extract_words(input_str, letter):
    """
    Extracts words from input_str that start with letter (case-sensitive) and contain at least two uppercase letters.
    
    Parameters:
    input_str (str): The input string to extract words from.
    letter (str): The single character that the extracted words should start with.
    
    Returns:
    list: A list of extracted words in uppercase.
    """
    pattern = r"\b" + letter + r"[A-Za-z]{1,}[A-Z]"
    matches = re.findall(pattern, input_str)
    extracted_words = [word.upper() for word in matches]
    return extracted_words