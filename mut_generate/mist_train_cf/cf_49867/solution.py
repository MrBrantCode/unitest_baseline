"""
QUESTION:
Develop a function `word_frequency(paragraph)` that takes a paragraph as input, calculates the frequency of each unique word (ignoring punctuation), and returns a dictionary where the keys are words and the values are their corresponding frequencies. The input paragraph is case-sensitive and words are separated by spaces. The function should handle punctuation next to words by removing it.
"""

def word_frequency(paragraph):
    # replacing punctuation marks with nothing to avoid confusion of same words with and without punctuation
    paragraph = paragraph.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    # splitting paragraph into list of words
    words = paragraph.split()
    # creating dictionary to store word frequencies
    frequency = {}
    for word in words:
        # if word is already in dictionary, increment its count
        if word in frequency:
            frequency[word] += 1
        # if word is not in dictionary, add it with count 1
        else:
            frequency[word] = 1
    # returning word frequency dictionary
    return frequency