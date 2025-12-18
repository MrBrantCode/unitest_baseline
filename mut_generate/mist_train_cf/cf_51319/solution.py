"""
QUESTION:
Write a function `find_nth_non_repeating_char(input_str, n)` that takes a string `input_str` and an integer `n` as input, and returns the nth non-repeating character in the string. A non-repeating character is a character that appears exactly once in the string. If there aren't that many non-repeating characters, return "None". The function should be case sensitive, i.e., 'A' and 'a' are considered two different characters. Optimize for both time and space complexity.
"""

def find_nth_non_repeating_char(input_str, n):
    """
    This function finds the nth non-repeating character in a given string.

    Args:
    input_str (str): The input string.
    n (int): The position of the non-repeating character to find.

    Returns:
    str: The nth non-repeating character if found, otherwise "None".
    """
    # Create a dictionary for frequency count of every character
    count = {}
    for char in input_str:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    # Iterate over the dictionary to find the nth non-repeating character
    non_repeating_chars = [char for char, freq in count.items() if freq == 1]
    if len(non_repeating_chars) < n:
        return "None"
    else:
        return non_repeating_chars[n-1]