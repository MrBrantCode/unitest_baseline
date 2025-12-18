"""
QUESTION:
Create a function called `remove_special_characters` that takes a string `s` as input and returns a new string with all special characters removed. The function should have a time complexity of O(n), be case-sensitive, preserve the case of the characters in the original string, and handle leading and trailing whitespace. It should not use built-in string manipulation functions like `replace()` or `translate()`, regular expressions, or external libraries, and should not create any intermediate strings during the removal process.
"""

def remove_special_characters(s):
    # Convert the string to a list of characters
    char_list = list(s)

    # Iterate over each character in the list
    i = 0
    while i < len(char_list):
        # Check if the character is alphanumeric
        if not char_list[i].isalnum():
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