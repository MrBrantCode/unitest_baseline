"""
QUESTION:
Create a function called `count_word_frequency` that takes a string of words as input. The function should count the frequency of each word in the string, ignoring case, punctuation marks, and special characters. The function should return a dictionary where the keys are the words and the values are their corresponding frequencies. The function should also handle words that are numbers.
"""

def count_word_frequency(word_string):
    word_string = word_string.lower()
    word_list = word_string.split()
    word_frequency = {}
    for word in word_list:
        word = ''.join(e for e in word if e.isalnum())
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency