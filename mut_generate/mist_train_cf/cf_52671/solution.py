"""
QUESTION:
Write a function `compare_sentences` that takes two sentences as input and returns the unique words in each sentence along with their counts. The function should split the sentences into words, count the occurrences of each word, and identify the words that are unique to each sentence.
"""

from collections import Counter

def compare_sentences(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    unique_words1 = counter1 - counter2
    unique_words2 = counter2 - counter1

    return unique_words1, unique_words2