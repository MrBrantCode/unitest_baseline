"""
QUESTION:
Write a function `change_case` that takes a string as input and returns a new string where all alphabetic characters have their case changed (i.e., uppercase to lowercase and vice versa), while non-alphabetic characters remain unchanged. The function should use a recursive approach and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def change_case(string):
    # Base case: if the string is empty, return an empty string
    if not string:
        return ""

    # Recursive case:
    # Get the first character of the string
    first_char = string[0]

    # Check if the first character is alphabetic
    if first_char.isalpha():
        # Change the case of the first character and concatenate it with the recursively processed remaining string
        return first_char.swapcase() + change_case(string[1:])
    else:
        # If the first character is not alphabetic, concatenate it as it is with the recursively processed remaining string
        return first_char + change_case(string[1:])