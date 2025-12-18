"""
QUESTION:
Write a function `can_be_palindrome` that determines if a given string can be converted into a palindrome by rearranging its characters. The function should return True if the string can be converted into a palindrome, False otherwise. The function should only consider the frequency of characters in the string and not their order, and it should ignore any case sensitivity and non-alphanumeric characters.
"""

def can_be_palindrome(s: str) -> bool:
    """
    This function determines if a given string can be converted into a palindrome 
    by rearranging its characters, ignoring case sensitivity and non-alphanumeric 
    characters.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string can be converted into a palindrome, False otherwise.
    """

    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(e for e in s if e.isalnum()).lower()

    # Create a frequency dictionary for characters in the string
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Count the number of characters that appear an odd number of times
    odd_count = 0
    for count in freq_dict.values():
        if count % 2 != 0:
            odd_count += 1

    # A string can be rearranged into a palindrome if at most one character appears 
    # an odd number of times
    return odd_count <= 1