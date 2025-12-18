"""
QUESTION:
Write a Python function `word_count(string)` that takes a string as input, removes punctuation marks, splits the string into a list of words, and returns a dictionary where the keys are the unique words found in the string (with a minimum length of 3 characters) and the values are the number of times each word appears. The word matching should be exact and case-sensitive.
"""

def word_count(string):
    # Remove punctuation marks from the string
    string = string.replace(".", "").replace(",", "").replace("!", "").replace("?", "")

    # Split the string into a list of words
    words = string.split()

    # Create an empty dictionary to store the word counts
    word_counts = {}

    # Iterate over each word in the list
    for word in words:
        # Ignore words that are less than 3 characters long
        if len(word) >= 3:
            # Update the count of the word in the dictionary
            word_counts[word] = word_counts.get(word, 0) + 1

    # Return the word counts dictionary
    return word_counts