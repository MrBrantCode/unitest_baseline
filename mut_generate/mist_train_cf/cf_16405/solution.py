"""
QUESTION:
Create a function named `capitalize_and_remove_duplicates` that takes a list of words as input. The function should capitalize each word in the list, removing any duplicates, and return the resulting list. Each word should have its first letter in uppercase and the rest of the letters in lowercase. The input list can contain up to 1000 words, each with a maximum length of 100 characters.
"""

def capitalize_and_remove_duplicates(words):
    """
    This function takes a list of words, capitalizes each word, removes duplicates, 
    and returns the resulting list. Each word has its first letter in uppercase and 
    the rest of the letters in lowercase.

    Args:
        words (list): A list of words.

    Returns:
        list: A list of capitalized words with no duplicates.
    """
    capitalized_words = []
    seen_words = set()
    
    for word in words:
        capitalized_word = word.capitalize()
        if capitalized_word not in seen_words:
            capitalized_words.append(capitalized_word)
            seen_words.add(capitalized_word)
    
    return capitalized_words