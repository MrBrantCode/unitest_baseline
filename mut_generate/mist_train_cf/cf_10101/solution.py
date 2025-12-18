"""
QUESTION:
Create a function `word_count` that takes a string as input and prints each word with its character count using a recursive approach. The function should ignore special characters and numbers, consider only alphabetic words, and handle leading or trailing spaces.
"""

def word_count(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Base case: if the string is empty, return
    if len(string) == 0:
        return

    # Check if the first character is a letter
    if string[0].isalpha():
        # Find the end index of the current word
        end_index = 1
        while end_index < len(string) and string[end_index].isalpha():
            end_index += 1

        # Print the current word and its character count
        print(string[:end_index], len(string[:end_index]))

        # Recursive call on the remaining string
        word_count(string[end_index:])

    else:
        # Recursive call on the remaining string
        word_count(string[1:])