"""
QUESTION:
Write a function called `reverse_and_remove_vowels` that takes a string as input, reverses it, and then removes all the vowels from the reversed string. The function should return the resulting string. The vowels to be removed include both lowercase and uppercase 'a', 'e', 'i', 'o', and 'u'.
"""

def reverse_and_remove_vowels(input_string):
    """
    Reverses a string and removes all the vowels from the reversed string.
    
    Parameters:
    input_string (str): The input string to be reversed and processed.
    
    Returns:
    str: The reversed string without vowels.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    reversed_string = input_string[::-1]
    return ''.join([char for char in reversed_string if char not in vowels])