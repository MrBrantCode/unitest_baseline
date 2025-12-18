"""
QUESTION:
Create a function named `create_word_dict` that takes a list of strings as input. The function should return a dictionary where each string in the list is a key and its corresponding value is the length of the string. However, if the length of the string is an odd number, the value should be multiplied by 2.
"""

def create_word_dict(words):
    """
    This function takes a list of strings and returns a dictionary where each string 
    is a key and its corresponding value is the length of the string. If the length 
    of the string is an odd number, the value is multiplied by 2.

    Args:
        words (list): A list of strings.

    Returns:
        dict: A dictionary where each string in the list is a key and its 
        corresponding value is the length of the string.
    """

    word_dict = {}
    for word in words:
        if len(word) % 2 == 0:
            word_dict[word] = len(word)
        else:
            word_dict[word] = len(word) * 2
    return word_dict