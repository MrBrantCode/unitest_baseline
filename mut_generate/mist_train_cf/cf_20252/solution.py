"""
QUESTION:
Write a function named `find_longest_word` that takes a sentence as input and returns the longest word that does not contain any duplicate letters and does not contain the letter 'e'.
"""

def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    longest_word = ""
    max_length = 0

    for word in words:
        if len(set(word)) != len(word) or 'e' in word.lower():
            continue

        if len(word) > max_length:
            max_length = len(word)
            longest_word = word

    return longest_word