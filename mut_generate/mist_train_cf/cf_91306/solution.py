"""
QUESTION:
Create a function named `count_word_frequency` that takes a sentence as input and returns the word frequency in descending order. The function should split the sentence into words, count the occurrences of each word, and return the result as a list of tuples, where each tuple contains the word and its frequency.
"""

def count_word_frequency(sentence):
    # Separating the words and storing them in an array
    words = sentence.lower().split()

    # Counting the occurrences of each word
    word_count = {}
    for word in words:
        word = word.strip('.,!?"\'')  # Remove punctuation
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # Sorting the words based on frequency in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_words