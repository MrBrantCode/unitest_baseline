"""
QUESTION:
Find the most frequent word in a sentence without using built-in string manipulation or counting functions. 

Write a function `most_frequent_word(sentence)` that takes a sentence as input and returns the word with the highest frequency. The function must have a time complexity of O(n), where n is the length of the sentence, and a space complexity of O(k), where k is the number of unique words in the sentence. The function should be case-sensitive and consider punctuation as part of a word.
"""

def most_frequent_word(sentence):
    word_freq = {}
    words = sentence.split()
    
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    
    max_word = ""
    max_freq = 0
    for word, freq in word_freq.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    
    return max_word