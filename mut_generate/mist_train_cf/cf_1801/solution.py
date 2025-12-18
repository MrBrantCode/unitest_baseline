"""
QUESTION:
Create a function `join_strings(words)` that takes a list of strings as input. The function should return a single sentence where each word from the input list is added in alternating case (lowercase, uppercase, lowercase, etc.), excluding any words that contain a vowel. If the input list is empty, raise a custom exception called "EmptyListException" with the message "The list cannot be empty."
"""

class EmptyListException(Exception):
    """Custom exception for empty list."""
    def __init__(self):
        super().__init__("The list cannot be empty.")

def join_strings(words):
    """
    Join a list of strings into a single sentence in alternating case, excluding any words that contain a vowel.
    
    Args:
        words (list): A list of strings.
    
    Returns:
        str: A sentence where each word from the input list is added in alternating case.
    
    Raises:
        EmptyListException: If the input list is empty.
    """
    if not words:
        raise EmptyListException()
    
    vowels = 'aeiou'
    result = []
    upper = True
    
    for word in words:
        if not any(char.lower() in vowels for char in word):
            result.append(word.upper() if upper else word.lower())
            upper = not upper
    
    return ' '.join(result)