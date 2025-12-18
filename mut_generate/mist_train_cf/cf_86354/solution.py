"""
QUESTION:
Create a function `remove_special_characters(s)` that takes a string `s` as input and returns a new string with all special characters removed. The function should have a time complexity of O(n), be case-sensitive, preserve leading and trailing whitespace, and not use any built-in string manipulation functions, regular expressions, or external libraries. The function should directly modify the input string in place and return it as the output.
"""

def remove_special_characters(s):
    # Convert the string to a list of characters
    char_list = list(s)

    # Iterate over each character in the list
    i = 0
    while i < len(char_list):
        # Check if the character is alphanumeric
        if not char_list[i].isalnum() and not char_list[i].isspace():
            # Remove the special character by shifting all subsequent characters one position to the left
            for j in range(i, len(char_list) - 1):
                char_list[j] = char_list[j + 1]

            # Reduce the length of the list by 1
            char_list.pop()
        else:
            # Move to the next character
            i += 1

    # Convert the list of characters back to a string
    modified_s = ''.join(char_list)

    return modified_s