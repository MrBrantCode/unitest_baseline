"""
QUESTION:
Create a function named `convert_to_ascii` that takes a string as input and returns a new string where all non-alphanumeric characters are replaced with their corresponding ASCII values.
"""

def convert_to_ascii(text):
    """
    This function takes a string as input and returns a new string where all non-alphanumeric characters are replaced with their corresponding ASCII values.
    
    Parameters:
    text (str): The input string
    
    Returns:
    str: The string with non-alphanumeric characters replaced with ASCII values
    """
    converted_text = ""
    for char in text:
        if not char.isalnum():  
            converted_text += str(ord(char))  
        else:
            converted_text += char  
    return converted_text