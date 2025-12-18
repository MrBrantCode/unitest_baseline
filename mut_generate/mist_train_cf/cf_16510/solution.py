"""
QUESTION:
Write a function `find_first_repeated_letter(string)` that finds the index of the first occurrence of a repeated letter in the given string, ignoring any whitespace characters. The index is 0-based and should return -1 if no repeated letters are found.
"""

def find_first_repeated_letter(string):
    # Remove whitespace characters from the string
    string = string.replace(" ", "")

    # Iterate through the characters in the modified string
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return i

    # If no repeated letters are found
    return -1