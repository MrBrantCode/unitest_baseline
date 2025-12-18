"""
QUESTION:
Write a function `find_word` that takes two parameters: a string and a word. Return the number of occurrences of the word in the string, ignoring any non-alphabetic characters and considering word boundaries (i.e., "Hello" is not considered part of "HelloWorld").
"""

def find_word(string, word):
    counter = 0
    word_length = len(word)
    string = ''.join(e for e in string if e.isalnum() or e.isspace()).lower()
    word = word.lower()
    for i in range(0, len(string)):
        if string[i:i+word_length] == word:
            counter += 1
    return counter