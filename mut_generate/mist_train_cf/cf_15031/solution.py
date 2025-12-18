"""
QUESTION:
Implement a function `parse_string(string)` that takes a string of words as input and returns an array of uppercase words in the order of their appearance. The string contains only alphabetic characters and spaces, with a length between 1 and 10^5. The function should not use built-in string parsing functions and have a time complexity of O(n), where n is the length of the string.
"""

def parse_string(string):
    words = []
    word = ''
    for char in string:
        if char != ' ':
            word += char
        else:
            if word.isupper():
                words.append(word)
            word = ''
    if word.isupper():
        words.append(word)
    return words