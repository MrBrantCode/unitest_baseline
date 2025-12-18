"""
QUESTION:
Write a function `concatenateAlphabets` that takes two string parameters, concatenates them, removes duplicate characters, sorts the result in alphabetical order, and returns the resulting string. The function should also handle case sensitivity by either treating upper and lower case letters as separate characters or converting all letters to lower case.
"""

def concatenateAlphabets(string1, string2):
    """
    Concatenates two strings, removes duplicate characters, sorts the result in alphabetical order, 
    and returns the resulting string. This function treats upper and lower case letters as separate characters.

    Args:
        string1 (str): The first string to concatenate.
        string2 (str): The second string to concatenate.

    Returns:
        str: A sorted string of concatenated input strings with duplicates removed.
    """
    # Concatenate the two strings
    concatenated_string = string1 + string2
    
    # Sort the string and remove duplicates
    sorted_string = ''.join(sorted(set(concatenated_string)))
    
    return sorted_string

# If you want to treat upper and lower case letters as the same character, 
# you can convert the strings to lower case before concatenation.
# Here is how you can modify the function to do that:

def concatenateAlphabets_lower(string1, string2):
    """
    Concatenates two strings, removes duplicate characters, sorts the result in alphabetical order, 
    and returns the resulting string. This function treats upper and lower case letters as the same character.

    Args:
        string1 (str): The first string to concatenate.
        string2 (str): The second string to concatenate.

    Returns:
        str: A sorted string of concatenated input strings with duplicates removed.
    """
    # Convert strings to lower case and concatenate the two strings
    concatenated_string = string1.lower() + string2.lower()
    
    # Sort the string and remove duplicates
    sorted_string = ''.join(sorted(set(concatenated_string)))
    
    return sorted_string