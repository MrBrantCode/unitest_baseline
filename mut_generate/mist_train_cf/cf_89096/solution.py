"""
QUESTION:
Write a function named `count_unique_words` that takes a string as input and returns the number of unique words. A word is a sequence of characters separated by whitespace, and punctuation marks (commas, periods, question marks, exclamation marks) are ignored. The function should count each unique word only once.
"""

def count_unique_words(string):
    # Remove punctuation marks from the string
    string = string.replace(",", "").replace(".", "").replace("?", "").replace("!", "")

    # Split the string into words
    words = string.split()

    # Create a set to store unique words
    unique_words = set()

    # Iterate over the words and add them to the set
    for word in words:
        unique_words.add(word)

    # Return the number of unique words
    return len(unique_words)