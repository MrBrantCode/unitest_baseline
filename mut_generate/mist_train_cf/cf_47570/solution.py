"""
QUESTION:
Write a function named `count_words` that takes two string arguments, `verse1` and `verse2`, representing two diverse verse extracts. The function should return a dictionary where the keys are the distinct words in the verses (case-insensitive) and the values are lists of two integers representing the occurrence count of each word in `verse1` and `verse2`, respectively. Note that punctuation should be considered part of the word.
"""

def count_words(verse1, verse2):
    words1 = verse1.lower().split()
    words2 = verse2.lower().split()

    word_dict = {}

    for word in words1:
        if word in word_dict:
            word_dict[word][0] += 1
        else:
            word_dict[word] = [1, 0]

    for word in words2:
        if word in word_dict:
            word_dict[word][1] += 1
        else:
            word_dict[word] = [0, 1]

    return word_dict