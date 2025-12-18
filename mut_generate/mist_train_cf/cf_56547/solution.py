"""
QUESTION:
Define a function `word_count` that accepts a string as input, including leading, trailing, and multiple consecutive whitespace characters. The function should disregard case, include special characters within the words, and return the total count of words present in the string. The function should also handle erroneous and incompatible inputs by returning an error message for None and non-string types.
"""

def word_count(s):
    """Define a function word_count, that accepts a string as an input, 
    provides the total count of words present within the string. Words 
    are identified as separate entities divided by whitespaces, including
    leading, trailing and multiple consecutive whitespaces. The case is 
    disregarded but include special characters within the words. 

    Check for None and non-string input types and return appropriate 
    error message.
    """
    if s is None:
        return 'Error: Input is None'
    elif type(s) != str:
        return 'Error: Input should be a string'

    # Removing leading and trailing whitespaces 
    # and replacing multiple consecutive whitespaces with a single space
    s = ' '.join(s.split())
                      
    return len(s.split(' '))