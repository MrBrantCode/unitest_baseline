"""
QUESTION:
Write a function `count_words(sentence)` that takes a sentence of at most 1000 characters as input. The function should separate the words, exclude common words ("the", "and", "it"), count the occurrences of each unique word, and return the result in descending order of frequency without using built-in functions, libraries, or regular expressions for counting occurrences, and with a time complexity of O(n log n), where n is the number of unique words.
"""

def count_words(sentence):
    # List of common words to exclude from counting
    common_words = ['the', 'and', 'it']

    # Removing punctuation marks and converting to lowercase
    sentence = sentence.replace('.', '').replace(',', '').lower()

    # Splitting the sentence into words
    words = sentence.split()

    # Dictionary to store word counts
    word_counts = {}

    # Counting occurrences of each unique word
    for word in words:
        if word not in common_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    # Sorting the words by their counts in descending order
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Returning the result
    return sorted_counts