"""
QUESTION:
Write a function `reverse_words` that takes a string as input, reverses each word in the string, and returns the resulting string. The words in the input string are separated by single spaces and may contain punctuation. The function should not use any built-in string manipulation methods or libraries, except for the `len` function.
"""

def reverse_words(string):
    words = []
    word = ""
    in_word = False
    
    for char in string:
        if char == " ":
            if in_word:
                words.append(word[::-1])
                word = ""
                in_word = False
        else:
            word += char
            in_word = True
    
    if in_word:
        words.append(word[::-1])
    
    return " ".join(words)