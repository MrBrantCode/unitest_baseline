"""
QUESTION:
Create a Python function named `word_count_func` that takes a string `text` as input and returns three values: 
- The number of unique words in the text.
- A dictionary containing the frequency of each unique word.
- A list of the three most frequent words.

The function should be case-insensitive and consider punctuation as part of the word. Do not use any external Python libraries.
"""

def word_count_func(text):
    # Split text into words
    words = text.split()

    # Create a dictionary to store words and their frequencies
    word_freq = {}

    # Iterate over each word in words
    for word in words: 
        # Convert word to lowercase
        word = word.lower()
        
        # If word is already in dictionary, increment its count
        if word in word_freq: 
            word_freq[word] += 1
        # If word is not in dictionary, add it with a count of 1
        else:
            word_freq[word] = 1

    # Get number of unique words
    num_unique_words = len(word_freq)

    # Get the three most frequent words
    most_frequent_words = sorted(word_freq, key = word_freq.get, reverse=True)[:3]

    return num_unique_words, word_freq, most_frequent_words