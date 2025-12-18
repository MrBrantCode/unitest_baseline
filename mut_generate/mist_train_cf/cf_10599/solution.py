"""
QUESTION:
Write a function named `is_sequence_of_words` that takes two parameters: `string` and `words_list`. The function should determine if `string` is a sequence of any of the words in `words_list` in the same order as they appear in the list, without using any built-in functions or libraries. The input string and words in the list are guaranteed to not contain spaces or special characters.
"""

def is_sequence_of_words(string, words_list):
    # Start with an empty sequence
    sequence = ""

    # Iterate over each character in the string
    for char in string:
        # Add the character to the sequence
        sequence += char

        # Check if the current sequence matches any of the words in the list
        if sequence in words_list:
            # If the current sequence is the last word in the list, return True
            if sequence == words_list[-1]:
                return True
            # Otherwise, continue to the next character
            sequence = ""

    # If we reach the end of the string and haven't found a match, return False
    return False