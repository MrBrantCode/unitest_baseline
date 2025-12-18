"""
QUESTION:
Write a function `count_non_printable_characters` that takes an input string and returns a tuple containing the count of non-printable characters and a list of the non-printable characters found in the string. Non-printable characters are those that cannot be displayed on the screen, including control characters, special characters, and whitespace characters, but excluding newline characters. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string. The function should not use any built-in functions or libraries that provide direct access to character encoding information or character classification.
"""

def entance(input_string):
    non_printable_chars = []
    count = 0
    
    for char in input_string:
        if (ord(char) < 32 and char != '\n') or ord(char) > 126:
            non_printable_chars.append(char)
            count += 1
    
    return count, non_printable_chars