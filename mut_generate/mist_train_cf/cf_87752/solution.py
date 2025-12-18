"""
QUESTION:
Extract the substring from a given string between two specified words. The substring must be at least 10 characters long, contain at least two uppercase letters, and have no repeated characters. The function name should be `extract_substring`.
"""

def extract_substring(sentence, start_word, end_word):
    """
    Extract the substring from a given sentence between two specified words.
    
    The substring must be at least 10 characters long, contain at least two uppercase letters, 
    and have no repeated characters.
    
    Args:
        sentence (str): The given sentence.
        start_word (str): The starting word.
        end_word (str): The ending word.
    
    Returns:
        str: The extracted substring if it meets the required conditions, otherwise None.
    """
    
    # Find the starting and ending indices of the substring
    start_index = sentence.index(start_word) + len(start_word)
    end_index = sentence.index(end_word)
    
    # Extract the substring
    substring = sentence[start_index:end_index]
    
    # Check if the substring meets the required conditions
    if (len(substring) >= 10 and 
        sum(1 for c in substring if c.isupper()) >= 2 and 
        len(set(substring)) == len(substring)):
        return substring
    else:
        return None