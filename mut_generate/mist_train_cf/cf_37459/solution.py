"""
QUESTION:
Create a function named `word_frequency` that takes a string `text` as input and returns a list of tuples. The list should contain unique words from the input string along with their frequencies, sorted in descending order of frequency. In case of a tie, the words should be sorted in ascending lexicographical order. The input text may contain lowercase and uppercase letters, spaces, and punctuation marks. Treat punctuation marks as part of the words they are attached to.
"""

def word_frequency(text):
    # Remove punctuation marks and convert text to lowercase
    text = text.lower()
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)

    # Split the text into words
    words = text.split()

    # Create a dictionary to store word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Sort the word frequencies in descending order of frequency and ascending lexicographical order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_word_freq