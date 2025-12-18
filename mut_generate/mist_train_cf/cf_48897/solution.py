"""
QUESTION:
Develop a function `lexicographical_distance` that accepts two strings as input and returns the lexicographical distance between them. The function should consider case sensitivity, handle Unicode characters, and account for strings of different lengths. The lexicographical distance is the number of character changes required to make the two strings identical, without considering the order of characters.
"""

import unicodedata

def lexicographical_distance(string1, string2):
    """
    Calculate the lexicographical distance between two strings.
    
    The lexicographical distance is the number of character changes required to make the two strings identical,
    without considering the order of characters. This function considers case sensitivity, handles Unicode characters,
    and accounts for strings of different lengths.
    
    Parameters:
    string1 (str): The first string.
    string2 (str): The second string.
    
    Returns:
    int: The lexicographical distance between the two strings.
    """
    len_str1 = len(string1)
    len_str2 = len(string2)
    
    count = 0

    # Unicode normalize
    string1 = unicodedata.normalize('NFC', string1)
    string2 = unicodedata.normalize('NFC', string2)
    
    # Case sensitive compare
    for i in range(min(len_str1, len_str2)):
        if(string1[i] != string2[i]):
            count += 1
    
    # If length is not same
    if(len_str1 != len_str2):
        count += abs(len_str1-len_str2)
    
    return count