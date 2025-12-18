"""
QUESTION:
Write a function `trace_words(s, words)` that takes a string `s` and a list of distinct words `words` as input, and returns a dictionary where the keys are the words from the list that appear in the string `s` and the values are their corresponding frequencies.
"""

def trace_words(s, words):
    instances = {}
    for word in words:
        count = s.count(word)
        if count > 0:
            instances[word] = count
    return instances