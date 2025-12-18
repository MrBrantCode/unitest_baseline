"""
QUESTION:
Write a function `word_frequency(words)` that takes a list of words as input and returns a dictionary containing the frequency of each word in the list. The function should be able to handle any list of words, including empty lists and lists with duplicate words. The output dictionary should map each unique word in the input list to its frequency, where the frequency is the number of times the word appears in the list.
"""

def entance(words):
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict