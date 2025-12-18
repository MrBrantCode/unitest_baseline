"""
QUESTION:
Write a function named `compress_string` that takes a string as input and returns a new string where consecutive duplicate characters are removed and the number of times each character appears consecutively is appended to the character. The function should not use any additional data structures and should have a time complexity of O(n), where n is the length of the input string. The input string will contain only uppercase and lowercase letters, can be of length up to 10^6 characters, and may have more than 9 consecutive occurrences of a character.
"""

def compress_string(s):
    """
    Compress a string by removing consecutive duplicate characters and appending the count.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The compressed string.
    """
    if not s:
        return ""

    compressed_string = ""
    count = 1
    previous_char = s[0]

    for char in s[1:]:
        if char == previous_char:
            count += 1
        else:
            compressed_string += previous_char
            if count > 1:
                compressed_string += str(count)
            count = 1
        previous_char = char

    compressed_string += previous_char
    if count > 1:
        compressed_string += str(count)

    return compressed_string