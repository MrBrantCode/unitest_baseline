"""
QUESTION:
Write a function named `count_word_frequencies` that takes a string as input and returns the frequency of each word, considering both uppercase and lowercase letters and excluding any punctuation marks. The function should optimize for space complexity. The input string may contain words separated by non-alphabetic characters, and the function should handle cases where the string ends with a word.
"""

def count_word_frequencies(string):
    word_freq = {}

    string = string.lower()
    word = ""

    for char in string:
        if char.isalpha():
            word += char
        else:
            if word:
                word_freq[word] = word_freq.get(word, 0) + 1
                word = ""

    if word:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq