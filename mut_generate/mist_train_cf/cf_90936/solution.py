"""
QUESTION:
Write a function `count_repeated_words` that takes a sentence as input and returns a dictionary containing the count of repeated words, excluding any words that contain the letter 'e'. The function should be case-sensitive and consider punctuation as part of a word.
"""

def count_repeated_words(sentence):
    words = sentence.split()
    count = {}
    
    for word in words:
        if 'e' not in word:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    
    return count