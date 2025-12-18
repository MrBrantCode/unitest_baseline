"""
QUESTION:
Find the index of the first repeated letter in a given string, ignoring any whitespace characters. The function should be named `find_first_repeated_letter` and should take a string as input. If no repeated letters are found, the function should return -1.
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