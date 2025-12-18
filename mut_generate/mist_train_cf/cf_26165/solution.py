"""
QUESTION:
Create a function called `count_words` that takes a string `s` as input. The function should return a dictionary where the keys are the unique words in the string and the values are their corresponding frequencies. The words should be case-sensitive.
"""

def count_words(s): 
    words = s.split() 
    returnCounter = dict.fromkeys(words, 0) 
    for word in words: 
        returnCounter[word] += 1
    return returnCounter