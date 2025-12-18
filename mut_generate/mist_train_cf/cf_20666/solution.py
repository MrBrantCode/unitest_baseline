"""
QUESTION:
Write a function named `count_words` that takes a list of sentences as input and returns a dictionary where the keys are the words and the values are the number of times each word appears in the list. The function should be case sensitive.
"""

def count_words(sentences):
    word_count = {}
    
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    return word_count