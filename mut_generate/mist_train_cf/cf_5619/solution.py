"""
QUESTION:
Implement a function `remove_duplicates(string: str) -> str` where `string` is a string of length 1 to 10^6 containing lowercase and/or uppercase alphabets and spaces. The function should return the input string with all duplicate words removed, preserving the original word order and separated by a single space.
"""

def remove_duplicates(string: str) -> str:
    """
    This function removes duplicate words from a given string, preserving the original word order.
    
    Args:
    string (str): The input string containing lowercase and/or uppercase alphabets and spaces.
    
    Returns:
    str: The input string with all duplicate words removed, separated by a single space.
    """
    unique_words = set()
    result = []
    
    # Split the input string into a list of words
    for word in string.split():
        # Add the word to the result list if it's not already in the set
        if word.lower() not in unique_words:
            result.append(word)
            unique_words.add(word.lower())
    
    # Join the unique words together with a space as the separator
    return ' '.join(result)