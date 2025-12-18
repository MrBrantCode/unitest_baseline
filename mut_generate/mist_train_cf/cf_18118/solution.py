"""
QUESTION:
Create a function `count_word_frequency` that takes a string of words as input, counts the frequency of each word while ignoring different cases and punctuation marks or special characters, and returns a dictionary where the word is the key and the frequency is the value.
"""

def count_word_frequency(word_string):
    # Remove punctuation and special characters
    word_string = ''.join(e for e in word_string if e.isalnum() or e.isspace())

    # Convert all words to lowercase
    word_string = word_string.lower()

    # Split the string into individual words
    words = word_string.split()

    # Count the frequency of each word
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency