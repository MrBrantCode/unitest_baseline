"""
QUESTION:
Create a function named `word_frequencies` that takes a string `text` as input and returns a dictionary where the keys are words longer than seven characters (after removing non-alphabetic characters and converting to lower case) and the values are their respective frequencies in the text.
"""

def word_frequencies(text):
    # Split the text into words
    words = text.split()

    # Create an empty dictionary to store the frequencies
    freq_dict = {}

    # Iterate over the words
    for word in words:
        # Ignore words less than 7 characters
        if len(word) < 7:
            continue

        # Filter out non-alphabetic characters and convert the word to lower case
        word = ''.join(filter(str.isalpha, word)).lower()

        # If the word is in the dictionary, increase its frequency by 1
        # If the word is not in the dictionary, add it with a frequency of 1
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    return freq_dict