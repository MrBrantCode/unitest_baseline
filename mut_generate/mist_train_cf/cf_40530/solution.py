"""
QUESTION:
Implement a function `split_by_length(wordlist)` that takes a non-empty list of non-empty strings `wordlist` as input and returns a dictionary where the keys are the lengths of the words and the values are lists of words with the corresponding length.
"""

def split_by_length(wordlist):
    result = {}
    for word in wordlist:
        word_length = len(word)
        if word_length in result:
            result[word_length].append(word)
        else:
            result[word_length] = [word]
    return result