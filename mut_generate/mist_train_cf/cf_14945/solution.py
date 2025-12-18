"""
QUESTION:
Write a function `removeLetters` that takes a string and a letter as input, and returns a new string with all instances of the given letter removed. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the string. Do not use any built-in functions or libraries for removing characters from the string.
"""

def removeLetters(string, letter):
    # Create an empty string to store the result
    result = ""

    # Iterate over each character in the string
    for char in string:
        # Check if the character is not the letter to be removed
        if char != letter:
            # Append the character to the result string
            result += char

    # Return the result string
    return result