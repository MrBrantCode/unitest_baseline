"""
QUESTION:
Calculate the length of each word in a given string, excluding punctuation marks, numbers, and special characters, and store them in a new array. The array should be in descending order of word lengths, with words of the same length sorted in reverse alphabetical order, and maintaining the original order for words with the same length and reverse alphabetical order. Implement a function named `word_lengths` that takes a string as input and returns the resulting array.
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