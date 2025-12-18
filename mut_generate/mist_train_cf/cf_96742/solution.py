"""
QUESTION:
Write a function named `word_count` that takes a list of words as input and returns a dictionary where the keys are the unique words and the values are the number of times each word appears in the list. The function should use a hashing algorithm to efficiently store and retrieve the word counts.
"""

def word_count(words):
    word_counts = {}  
    for word in words:
        if word in word_counts:
            word_counts[word] += 1  
        else:
            word_counts[word] = 1  
    return word_counts