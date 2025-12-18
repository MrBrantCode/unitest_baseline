"""
QUESTION:
Create a function called `format_string` that capitalizes the first letter of each word in a given string while keeping the rest of the letters lowercase, without affecting punctuation marks. The function should return the formatted string, truncated to a maximum length of 100 characters if necessary.
"""

def format_string(s):
    """
    Capitalizes the first letter of each word in a given string while keeping the rest of the letters lowercase, 
    without affecting punctuation marks. The function returns the formatted string, truncated to a maximum length 
    of 100 characters if necessary.

    Args:
        s (str): The input string to be formatted.

    Returns:
        str: The formatted string.
    """
    # Split the string into words and punctuation marks
    words = s.split()
    
    # Capitalize the first letter of each word while keeping the rest of the letters lowercase
    formatted_words = [word[0].upper() + word[1:].lower() for word in words]
    
    # Join the formatted words back into a string
    formatted_string = ' '.join(formatted_words)
    
    # Truncate the string to a maximum length of 100 characters if necessary
    formatted_string = formatted_string[:100]
    
    return formatted_string