"""
QUESTION:
Write a function `find_most_frequent_word(sentence)` that takes a sentence as input and returns the most frequent word in the sentence, ignoring case and punctuation. The function must have a time complexity of O(n) and a space complexity of O(k), where n is the length of the sentence and k is the number of unique words in the sentence. The solution must not use any built-in functions or libraries for string manipulation or counting occurrences.
"""

import re

def find_most_frequent_word(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    words = sentence.split()
    word_count = {}
    max_count = 0
    most_frequent_word = ''

    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
        if word_count[word] > max_count:
            max_count = word_count[word]
            most_frequent_word = word
            
    return most_frequent_word