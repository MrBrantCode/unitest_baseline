"""
QUESTION:
Write a function named `oblit_alpha` that takes a string and an index as input and returns the modified string with the first alphabetic character starting from the given index removed, along with the position where the character was found. If the character at the specified index is not an alphabet, the function should continue to the next character until an alphabet is deleted. If no alphabet is found, return the original string and -1 as the position.
"""

def oblit_alpha(string, index):
    # Parsing until an alphabet is found and removed
    while index < len(string) and not string[index].isalpha():
        index += 1

    # Return the string if no alphabet is found
    if index >= len(string):
        return string, -1

    # Return the resultant string by deleting the alphabet
    return string[:index] + string[index+1:], index