"""
QUESTION:
Write a function named `common_words` that takes two strings as input and returns a list of common words between them. The function should ignore case sensitivity, exclude punctuation marks, remove any duplicate words, and sort the resulting list alphabetically. Assume that the input strings will only contain alphabetic characters, spaces, and punctuation marks.
"""

import string

def common_words(string1, string2):
    """
    This function takes two strings as input, removes any punctuation marks, 
    converts them to lowercase, and returns a list of common words between them.
    
    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.
    
    Returns:
        list: A list of common words between the two input strings.
    """
    
    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Remove any punctuation marks from both strings
    string1 = string1.translate(str.maketrans("", "", string.punctuation))
    string2 = string2.translate(str.maketrans("", "", string.punctuation))

    # Split both strings into individual words
    words1 = string1.split()
    words2 = string2.split()

    # Find the common words between the two lists
    common_words = sorted(list(set(words1) & set(words2)))

    return common_words