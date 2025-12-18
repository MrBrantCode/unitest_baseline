"""
QUESTION:
Write a function `remove_longest_word(sentence)` that takes a sentence as input and returns the string with all occurrences of the longest word(s) removed. The input sentence is a string of space-separated words. If there are multiple words with the same length as the longest word, remove all of them. If there are no words in the sentence, return an empty string.
"""

def remove_longest_word(sentence):
    words = sentence.split()
    if len(words) == 0:
        return ""
    max_length = max(len(word) for word in words)
    filtered_words = [word for word in words if len(word) != max_length]
    return " ".join(filtered_words)