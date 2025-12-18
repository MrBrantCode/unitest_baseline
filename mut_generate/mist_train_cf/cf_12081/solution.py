"""
QUESTION:
Convert the given list of strings to a single string where each word is capitalized, without using the "join" method, and remove any trailing whitespace.
"""

def capitalize_words(str_list):
    """
    Converts the given list of strings to a single string where each word is capitalized.
    
    Args:
        str_list (list): A list of strings.
    
    Returns:
        str: A single string where each word is capitalized.
    """
    result = ""
    for word in str_list:
        result += word.capitalize() + " "
    return result.strip()