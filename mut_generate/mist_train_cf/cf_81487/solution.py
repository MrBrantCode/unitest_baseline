"""
QUESTION:
Create a function called `split_string_into_words` that takes a string as input and returns a list of words. The function should split the input string into individual words, disregard any punctuation attached to the words, and convert all resultant words to lower case. The function should not use any built-in Python libraries or methods.
"""

def split_string_into_words(input_string):
    punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\t', '\n']

    words = []
    word = ""
    for character in input_string.lower():
        if character not in punctuation and character != ' ':
            word += character
        else:
            if word != "":
                words.append(word)
            word = ""
    if word != "":
        words.append(word)
    return words