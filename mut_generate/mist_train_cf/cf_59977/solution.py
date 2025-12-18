"""
QUESTION:
Implement a Python function `string_to_upper` that takes a string `input_string` as input and returns the string with all alphabetic characters in uppercase, while preserving the original case of words that are already partially or fully uppercase. The function must correctly handle words with hyphenations, apostrophes, punctuation marks, special characters, and alphanumeric combinations.
"""

import re

def string_to_upper(input_string):
    """
    This function takes a string as input and returns the string with all alphabetic characters in uppercase, 
    while preserving the original case of words that are already partially or fully uppercase.
    
    It handles words with hyphenations, apostrophes, punctuation marks, special characters, and alphanumeric combinations.
    
    Parameters:
    input_string (str): The input string that needs to be converted.
    
    Returns:
    str: The string with all alphabetic characters in uppercase.
    """
    # Split the input string into words and non-word characters
    words = re.split('(\W)', input_string)
    
    # Initialize an empty list to store the processed words
    processed_words = []
    
    # Iterate over each word in the input string
    for word in words:
        # Check if the word is alphabetic
        if word.isalpha():
            # If the word is already uppercase, add it as it is
            if word.isupper():
                processed_words.append(word)
            # If the word is not uppercase, convert it to uppercase
            else:
                processed_words.append(word.upper())
        # If the word is not alphabetic, check if it's alphanumeric
        elif word.isalnum():
            # Convert the alphabetic characters in the alphanumeric word to uppercase
            processed_words.append(''.join(c.upper() if c.isalpha() else c for c in word))
        # If the word is neither alphabetic nor alphanumeric, add it as it is
        else:
            processed_words.append(word)
    
    # Join the processed words back into a string
    output_string = ''.join(processed_words)
    
    return output_string