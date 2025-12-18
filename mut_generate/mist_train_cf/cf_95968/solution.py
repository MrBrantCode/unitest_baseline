"""
QUESTION:
You need to implement a function named `count_unique_words` that takes a string of words separated by spaces as input, ignoring case sensitivity, punctuation, and special characters, and treating plural, possessive words, and contractions as the same word. The function should return the count of unique words without using any built-in functions or libraries.
"""

def count_unique_words(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Initialize a set to store unique words
    unique_words = set()

    # Initialize variables to keep track of the current word and whether a word is being formed
    current_word = ''
    is_forming_word = False

    # Iterate over each character in the string
    for char in string:
        # Check if the character is an alphabetic character or an apostrophe
        if char.isalpha() or char == "'":
            # Append the character to the current word
            current_word += char
            is_forming_word = True
        else:
            # Check if a word is being formed
            if is_forming_word:
                # Add the current word to the set of unique words
                unique_words.add(current_word.lower())

                # Reset the current word and is_forming_word variables
                current_word = ''
                is_forming_word = False

    # Check if a word is being formed after iterating through all the characters
    if is_forming_word:
        # Add the current word to the set of unique words
        unique_words.add(current_word.lower())

    # Return the count of unique words
    return len(unique_words)