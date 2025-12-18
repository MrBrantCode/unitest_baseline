"""
QUESTION:
Write a function `remove_longest_word` that takes a sentence as input and returns the sentence with all occurrences of the longest word(s) removed. If the input sentence is empty, return an empty string.
"""

def remove_longest_word(sentence):
    words = sentence.split()
    if len(words) == 0:
        return ""
    longest_length = max(len(word) for word in words)
    new_sentence = ""
    for word in words:
        if len(word) != longest_length:
            new_sentence += word + " "
    return new_sentence.strip()