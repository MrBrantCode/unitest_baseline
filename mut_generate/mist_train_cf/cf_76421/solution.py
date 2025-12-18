"""
QUESTION:
Write a function called `most_frequent_word` that takes a string as input and returns the most frequently occurring word in the string. The function should consider case sensitivity and punctuation as part of the word. The input string may contain multiple words with the same maximum frequency, in which case any one of them can be returned.
"""

def most_frequent_word(sentence):
    words = sentence.split()
    word_count_dict = {}
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
            
    max_count = 0
    most_frequent_word = ""
    for word, count in word_count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word
            
    return most_frequent_word