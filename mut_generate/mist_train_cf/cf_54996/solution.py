"""
QUESTION:
Create a function named word_count that takes a string as input and computes the total quantity of words that the string contains. A word is identified as a separate entity partitioned by whitespaces. Case sensitivity is ignored, however, special characters within words are included. The function should handle inputs with varying amounts of whitespace characters, and it should return an error message for non-string inputs.
"""

import re

def word_count(s):
    """Computes the total quantity of words in the input string, 
    ignoring case sensitivity but including special characters within words.

    Args:
        s (str): The input string.

    Returns:
        int: The number of words in the string, or an error message if input is not a string.
    """
    if type(s) != str:      # makesure the input is a string
        return "Error: Input should be a string"
        
    if s.strip()=="":       # checks if the string is not empty or just whitespaces
        return 0
            
    words = re.findall(r'\S+', s)      # finds all the separate words using regular expression
    return len(words)