"""
QUESTION:
Create a function `delete_non_consonant_names` that takes a list of names as input and returns a new list containing only the names that end with a consonant (both lowercase and uppercase). Assume the input list only contains strings.
"""

def delete_non_consonant_names(names):
    """
    This function takes a list of names and returns a new list containing only the names that end with a consonant.

    Parameters:
    names (list): A list of names

    Returns:
    list: A list of names that end with a consonant
    """
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    return [name for name in names if name[-1] in consonants]