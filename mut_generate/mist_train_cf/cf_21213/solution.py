"""
QUESTION:
Create a function named `countUniqueAlphabets` that takes a string as input and returns the number of unique English alphabets present in the string, ignoring case sensitivity and non-alphabet characters.
"""

def countUniqueAlphabets(s):
    """
    Returns the number of unique English alphabets present in the string, 
    ignoring case sensitivity and non-alphabet characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The count of unique alphabets.
    """
    uniqueAlphabets = set()
    lowercaseString = s.lower()
    
    for character in lowercaseString:
        if 'a' <= character <= 'z' and character not in uniqueAlphabets:
            uniqueAlphabets.add(character)
    
    return len(uniqueAlphabets)