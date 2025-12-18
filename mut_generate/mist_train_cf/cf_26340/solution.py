"""
QUESTION:
Create a function named `parseUppercaseWords` that takes a string of words as input and returns a list containing only the words that are in uppercase. The words in the string may be separated by spaces and may contain a mix of uppercase and lowercase letters. The function should return an empty list if there are no uppercase words in the input string.
"""

def parseUppercaseWords(s):
    """
    This function takes a string of words as input and returns a list containing only the words that are in uppercase.
    
    Parameters:
    s (str): The input string of words.
    
    Returns:
    list: A list of words that are in uppercase.
    """
    return [word for word in s.split() if word.isupper()]