"""
QUESTION:
Implement a function `extract_last_two_words` that takes a string of words as input, where each word is separated by a single space, and returns the last two words in the string. The input string must contain at least three words, and the function should ignore any leading or trailing spaces. If the string contains less than three words, return an error message indicating that the input string must contain at least three words.
"""

def extract_last_two_words(words):
    # Remove leading and trailing spaces
    words = words.strip()

    # Split the string into words
    word_list = words.split()

    # Check if there are at least three words
    if len(word_list) < 3:
        return "Input string must contain at least three words"

    # Extract the last two words
    last_word = word_list[-1]
    second_last_word = word_list[-2]

    return second_last_word, last_word