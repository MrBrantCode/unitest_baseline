"""
QUESTION:
Write a function named `count_unique_words` that takes a sentence as an argument and returns a dictionary of all the unique words and their counts in the sentence. The function should be case-insensitive, ignore any punctuation marks, and have a time complexity of O(n), where n is the length of the sentence. The function should not use any built-in functions or libraries that directly solve the problem. The input sentence can be up to 10^6 characters long.
"""

def count_unique_words(sentence):
    word_counts = {}
    sentence = sentence.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")
    sentence = sentence.lower()
    words = sentence.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts