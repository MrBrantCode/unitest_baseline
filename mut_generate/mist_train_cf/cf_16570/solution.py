"""
QUESTION:
Write a function named `count_unique_words` that takes a sentence as an argument and returns a dictionary of all the unique words and their counts in the sentence, ignoring case sensitivity and punctuation marks. The function should have a time complexity of O(n), where n is the length of the sentence, and should not use any built-in functions or libraries that directly solve the problem.
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