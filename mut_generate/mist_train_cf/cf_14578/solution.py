"""
QUESTION:
Create a function `capitalize_words` that takes a string as input, removes all punctuation, and capitalizes the first letter of each word.
"""

def capitalize_words(text):
    """
    This function takes a string, removes punctuation and capitalizes the first letter of each word.
    
    Parameters:
    text (str): Input string
    
    Returns:
    str: Modified string with no punctuation and capitalized words
    """
    import string
    
    # Remove punctuation from the string
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the string into words
    words = text_no_punct.split()
    
    # Capitalize the first letter of each word and join them back into a string
    capitalized_text = ' '.join(word.capitalize() for word in words)
    
    return capitalized_text