"""
QUESTION:
Create a function named `word_count` that takes a string as input and returns a dictionary where each unique word is a key and its value is the number of times it appears in the string. The function should be case insensitive and ignore punctuation, and it must have a time complexity of O(n), where n is the length of the input string.
"""

def word_count(string):
    # Remove punctuation and convert to lowercase
    string = string.lower()
    string = ''.join(e for e in string if e.isalnum() or e.isspace())

    # Split string into words
    words = string.split()

    # Create dictionary to store word counts
    word_counts = {}

    # Count the number of occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts