"""
QUESTION:
Create a function called `remove_vowels_and_uppercase` that takes a list of strings as input. The function should return a new list where each string is converted to uppercase and has all vowels removed. Vowels are case-insensitive and include 'a', 'e', 'i', 'o', 'u'. The input list is not empty and contains only strings.
"""

def remove_vowels_and_uppercase(lst):
    """
    This function takes a list of strings, converts each string to uppercase, 
    and removes all vowels from each string.

    Args:
        lst (list): A list of strings.

    Returns:
        list: A new list of strings with vowels removed and converted to uppercase.
    """
    new_lst = []
    for word in lst:
        new_word = "".join([letter.upper() for letter in word if letter.lower() not in "aeiou"])
        new_lst.append(new_word)
    return new_lst