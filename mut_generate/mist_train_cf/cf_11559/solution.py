"""
QUESTION:
Create a function `find_longest_word` that takes a sentence as input and returns the longest word without the letter 'a'.
"""

def find_longest_word(sentence):
    longest_word = ""
    sentence = sentence.split()

    for word in sentence:
        if 'a' not in word and len(word) > len(longest_word):
            longest_word = word

    return longest_word