"""
QUESTION:
Write a function `word_lengths` that takes a string as input, calculates the length of each word, and returns an array of these lengths in descending order. If multiple words have the same length, sort them in reverse alphabetical order. If two words have the same length and reverse alphabetical order, maintain their original order. The input string may contain punctuation marks, numbers, and special characters.
"""

def word_lengths(string):
    # Remove punctuation marks, numbers, and special characters
    string = ''.join(c for c in string if c.isalpha() or c.isspace())

    # Split the string into words
    words = string.split()

    # Calculate the length of each word and store them in a dictionary
    lengths = {}
    for word in words:
        length = len(word)
        if length not in lengths:
            lengths[length] = []
        lengths[length].append(word)

    # Sort the lengths in descending order
    sorted_lengths = sorted(lengths.keys(), reverse=True)

    # Sort words with the same length in reverse alphabetical order
    sorted_words = []
    for length in sorted_lengths:
        sorted_words.extend(sorted(lengths[length], reverse=True))

    # Create the final output array
    output = []
    for word in sorted_words:
        output.append(len(word))

    return output