"""
QUESTION:
Write a function `check_alphabet_order(s)` that checks if a given string `s` contains all the alphabets in a specific order. The alphabets must appear consecutively and in the same order as they do in the English alphabet. The input string may contain uppercase and lowercase letters.
"""

def check_alphabet_order(s):
    # Convert the string to lowercase
    s = s.lower()

    # Initialize a variable to keep track of the current expected character
    expected_char = 'a'

    # Iterate over each character in the string
    for char in s:
        # If the current character matches the expected character, move to the next expected character
        if char == expected_char:
            expected_char = chr(ord(expected_char) + 1)
        
        # If we have reached 'z' (the last character), return True
        if expected_char == '{':
            return True
    
    # If we reach here, it means we did not find all the characters in order
    return False