"""
QUESTION:
Write a function `count_word_occurrence(sentence, word)` to count the number of times a specific word appears in a given sentence, without using built-in string manipulation functions. The function should handle cases where the word appears as part of another word, and it should be case-insensitive.
"""

def count_word_occurrence(sentence, word):
    count = 0
    sentence = sentence.lower()  # convert the sentence to lowercase
    word = word.lower()  # convert the word to lowercase

    # iterate through the sentence
    for i in range(len(sentence)):
        # check if current character is a word separator or punctuation
        if sentence[i] == ' ' or sentence[i] in ['.', ',', '?', '!', ';', ':']:
            # if the previous word is the desired word, increment count
            if sentence[i-len(word):i] == word:
                count += 1

    # handle case where the desired word is at the end of the sentence
    if sentence[len(sentence)-len(word):] == word:
        count += 1

    return count