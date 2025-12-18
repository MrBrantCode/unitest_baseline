"""
QUESTION:
Write a function named `count_words` that takes a sentence of at most 1000 characters as input, counts the occurrences of each unique word excluding common words like "the", "and", and "it", and returns the words and their counts in descending order of frequency. The function should not use built-in functions, libraries, or regular expressions for counting occurrences, and it should have a time complexity of O(n log n), where n is the number of unique words in the sentence.
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

    return sorted_counts