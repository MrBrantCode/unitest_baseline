"""
QUESTION:
Implement the function `remove_vowels_digits_punctuation_whitespace(text)` that takes a string `text` and returns a string containing only the consonants from `text`, excluding vowels, digits, punctuation marks, and whitespace characters. The function should handle both lowercase and uppercase letters.
"""

def remove_vowels_digits_punctuation_whitespace(text):
    """
    remove_vowels_digits_punctuation_whitespace is a function that takes a string and returns a string without vowels, digits, punctuation marks, and whitespace characters.
    
    Parameters:
    text (str): The input string to process.
    
    Returns:
    str: A string containing only the consonants from the input string.
    """
    
    # List of vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    # Import string module to get punctuation marks
    import string
    
    # Store punctuation marks
    punctuation_marks = string.punctuation
    
    # Initialize an empty string to store consonants
    consonants = ""
    
    # Loop through text
    for i in text:
        # If i is not a digit, whitespace, vowel, or punctuation mark
        if not (i.isdigit() or i.isspace() or i in vowels or i in punctuation_marks):
            consonants += i
    
    return consonants