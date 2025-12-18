"""
QUESTION:
Write a function named `count_unique_chars_and_check_anagrams` that takes two string parameters, checks if they are anagrams of each other (ignoring case and spaces), and counts the number of unique characters used in the anagrams. The function should return a boolean value indicating whether the strings are anagrams and an integer representing the number of unique characters.
"""

def count_unique_chars_and_check_anagrams(str1, str2):
    """
    Checks if two strings are anagrams of each other (ignoring case and spaces) 
    and counts the number of unique characters used in the anagrams.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        tuple: A boolean indicating whether the strings are anagrams and an integer 
        representing the number of unique characters.
    """

    str1 = str1.replace(" ","").lower()  # Remove spaces and convert to lowercase
    str2 = str2.replace(" ","").lower()
    
    # Check if sorted characters are the same (meaning they are anagrams)
    if sorted(str1) == sorted(str2):
        is_anagram = True
    else:
        is_anagram = False
    
    # Concatenate the strings and convert to a set to remove duplicates,
    # then count the number of characters
    unique_chars = len(set(str1+str2))

    return is_anagram, unique_chars