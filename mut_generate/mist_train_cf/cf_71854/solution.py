"""
QUESTION:
Create a function `replace_words` that takes a string `text` as input. Replace all words with 4 letters or more in the text with "*****". Return the modified string.
"""

def replace_words(text):
    words = text.split()
    for i in range(len(words)):
        if len(words[i]) >= 4:  
            words[i] = '*****'
    return ' '.join(words)