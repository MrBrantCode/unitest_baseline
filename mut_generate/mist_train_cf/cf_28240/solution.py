"""
QUESTION:
Implement a function `count_unique_words(pagedata)` that takes a list of strings `pagedata`, where each string represents the content of a web page. Return a dictionary where the keys are the page numbers (starting from 1) and the values are dictionaries containing the count of unique words on each page, considering words as case-sensitive and punctuation as part of the word.
"""

def count_unique_words(pagedata):
    result = {}
    for i, page in enumerate(pagedata, start=1):
        words = page.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        result[i] = len(word_count)
    return result