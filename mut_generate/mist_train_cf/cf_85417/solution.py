"""
QUESTION:
Create a function called `count_and_reverse` that takes two parameters: a string `input_string` and a single character `letter`. The function should return a tuple containing the count of `letter` in `input_string` (case-insensitive and ignoring non-alphabetic characters) and the reversed `input_string`.
"""

def count_and_reverse(input_string, letter):
    """
    This function takes a string and a character as input, 
    counts the occurrences of the character in the string (case-insensitive and ignoring non-alphabetic characters), 
    and returns the reversed string.

    Parameters:
    input_string (str): The input string.
    letter (str): The character to be counted.

    Returns:
    tuple: A tuple containing the count of the character in the string and the reversed string.
    """
    input_string = ''.join(filter(str.isalpha, input_string.lower()))
    letter = letter.lower()
    
    letter_count = input_string.count(letter)
    reversed_string = input_string[::-1]
    
    return letter_count, reversed_string