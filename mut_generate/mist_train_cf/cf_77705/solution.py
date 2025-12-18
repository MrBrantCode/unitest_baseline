"""
QUESTION:
Write a function `count_words` that takes a sentence as input and returns a dictionary where the keys are the distinct words in the sentence and the corresponding values are the occurrences of each word. The function should treat words with punctuation as distinct from the same word without punctuation and should be case-insensitive.
"""

def count_words(sentence):
    sentence = sentence.lower()
    occurrences = {}
    words = sentence.split()

    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1

    return occurrences