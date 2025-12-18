"""
QUESTION:
Write a function named `invert_string_words` that takes a string of space-separated words as input. The function should return a new string where each word is reversed, and if the word has an even number of characters, remove the middle character.
"""

def invert_string_words(string):
    words = string.split()
    inverted_words = []

    for word in words:
        if len(word) % 2 == 0:
            middle_index = len(word) // 2
            inverted_word = word[middle_index-1::-1] + word[middle_index+1:][::-1]
        else:
            inverted_word = word[::-1]  

        inverted_words.append(inverted_word)

    inverted_string = " ".join(inverted_words)
    return inverted_string