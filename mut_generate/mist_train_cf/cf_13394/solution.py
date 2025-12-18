"""
QUESTION:
Create a function `remove_vowels_uppercase_first` that takes a list of strings as input. The function should return a new list of strings where all strings have an uppercase first letter (if the original string is not empty) and do not contain any vowels. The original list should not be modified. Vowels are 'a', 'e', 'i', 'o', 'u' and their uppercase counterparts.
"""

def remove_vowels_uppercase_first(strings):
    """
    This function takes a list of strings, removes all vowels from each string, 
    and uppercases the first letter of each string (if it's not empty).
    
    Args:
    strings (list): A list of strings.
    
    Returns:
    list: A new list of strings with vowels removed and first letter uppercased.
    """
    new_list = []
    for string in strings:
        new_string = "".join(char for char in string if char.lower() not in 'aeiou')
        if new_string:
            new_string = new_string[0].upper() + new_string[1:]
        new_list.append(new_string)
    return new_list