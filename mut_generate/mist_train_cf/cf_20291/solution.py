"""
QUESTION:
Create a function `join_strings` that takes two strings `string1` and `string2` as input. The function should return the concatenation of `string1` in uppercase and `string2`, but only if `string1` is at least 8 characters long and `string2` contains no numbers. If either condition is not met, the function should return `None` and print an error message.
"""

def join_strings(string1, string2):
    """
    Returns the concatenation of string1 in uppercase and string2 if string1 is at least 8 characters long and string2 contains no numbers.
    
    Args:
        string1 (str): The first string to be concatenated.
        string2 (str): The second string to be concatenated.
    
    Returns:
        str or None: The concatenated string if conditions are met, otherwise None.
    """
    # Check if the length of String1 is at least 8 characters long
    if len(string1) < 8:
        print("String1 should be at least 8 characters long.")
        return None
    
    # Check if String2 contains any numbers
    if any(char.isdigit() for char in string2):
        print("String2 should not contain any numbers.")
        return None
    
    # Convert String1 to uppercase
    string1 = string1.upper()
    
    # Join String1 and String2
    result = string1 + string2
    
    return result