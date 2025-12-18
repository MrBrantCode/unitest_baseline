"""
QUESTION:
Write a function `join_strings(string1, string2)` that joins two input strings. The function should check if `string1` has a length of at least 12 characters and contains at least one special character. It should convert `string2` to lowercase and remove all vowels before joining the two strings. The final joined string should be reversed before being returned. If `string1` does not meet the requirements, the function should return without joining the strings.
"""

def join_strings(string1, string2):
    """
    Joins two input strings after performing certain operations.
    
    It checks if string1 has a length of at least 12 characters and contains at least one special character.
    Then it converts string2 to lowercase and removes all vowels before joining the two strings.
    The final joined string is reversed before being returned.
    
    If string1 does not meet the requirements, the function returns without joining the strings.

    Parameters:
    string1 (str): The first input string.
    string2 (str): The second input string.

    Returns:
    str: The joined string if string1 meets the requirements, otherwise None.
    """
    if len(string1) < 12 or not any(char in '!@#$%^&*()_-+=~`/.,<>?;:' for char in string1):
        return

    vowels = ['a', 'e', 'i', 'o', 'u']
    string2 = string2.lower()
    string2 = ''.join(char for char in string2 if char not in vowels)

    final_string = string1 + string2
    final_string = final_string[::-1]

    return final_string