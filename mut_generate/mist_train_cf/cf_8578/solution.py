"""
QUESTION:
Write a function `count_non_printable_characters` that takes an input string and returns a tuple containing the count of non-printable characters and a list of the non-printable characters found in the string. A non-printable character is any character that cannot be displayed on the screen, including control characters, special characters, and whitespace characters (excluding newline characters). The function should handle multi-line strings and count each non-printable character occurrence separately, and it should be able to handle strings with a length of up to 1 million characters efficiently with a time complexity of O(n) and a space complexity of O(1).
"""

def count_non_printable_characters(input_string):
    non_printable_chars = []
    count = 0
    
    for char in input_string:
        # Check if the character is a non-printable character
        if (ord(char) < 32 and char != '\n') or ord(char) > 126:
            non_printable_chars.append(char)
            count += 1
    
    return count, non_printable_chars