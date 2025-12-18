"""
QUESTION:
Write a function called `reverse_words` that takes a string input, reverses the order of its words, and excludes any consecutive duplicate words in the reversed string.
"""

def reverse_words(string):
    words = string.split()  
    reversed_words = ' '.join(reversed(words))  
    unique_words = []
    prev_word = None
    for word in reversed_words.split():
        if word != prev_word:
            unique_words.append(word)
        prev_word = word
    return ' '.join(unique_words)