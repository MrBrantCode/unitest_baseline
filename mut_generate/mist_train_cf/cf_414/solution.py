"""
QUESTION:
Write a function `count_word_frequencies` that takes a string as input and returns a dictionary where the keys are the unique words in the string (case-insensitive) and the values are their corresponding frequencies. The function should ignore punctuation marks and optimize for space complexity. The input string may contain multiple spaces between words, and the function should handle this correctly.
"""

def count_word_frequencies(string):
    word_freq = {}

    string = string.lower()
    word = ""

    for char in string:
        if char.isalpha() or char.isspace():
            if char.isspace():
                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1
                    word = ""
            else:
                word += char
        else:
            if word:
                word_freq[word] = word_freq.get(word, 0) + 1
                word = ""

    if word:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq