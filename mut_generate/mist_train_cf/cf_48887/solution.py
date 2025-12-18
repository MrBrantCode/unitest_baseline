"""
QUESTION:
Create a function called `count_words` that takes a string `text` as input and returns a dictionary where the keys are the unique words in the text and the values are their corresponding frequencies. The function should be case-insensitive and consider punctuation as part of a word.
"""

def count_words(text):
    text = text.lower().split()
    wordcount = {}
    for word in text:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount