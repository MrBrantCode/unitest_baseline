"""
QUESTION:
Create a function `count_characters(sentence)` that takes a sentence as input and returns a list containing the number of characters in each word of the sentence, excluding punctuation marks. The function should consider punctuation marks and special characters as separate words, handle multiple consecutive spaces or tabs between words, leading or trailing whitespace characters, uppercase and lowercase letters, and non-ASCII characters. The time complexity of the solution should be O(n), where n is the length of the sentence, and it should not use any built-in functions or libraries for splitting the sentence into words.
"""

def count_characters(sentence):
    words = []
    current_word = 0
    word_length = 0

    for char in sentence:
        if char.isalnum():
            word_length += 1
        elif word_length > 0:
            words.append(word_length)
            word_length = 0

    if word_length > 0:
        words.append(word_length)

    return words