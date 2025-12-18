"""
QUESTION:
Write a function named `reverse_sentence` that takes a string sentence as input and returns a string where every second word in the sentence is reversed. The reversal should be done in place, without adding or removing any words, and the case of the letters should remain the same.
"""

def reverse_sentence(sentence):
    words = sentence.split()  # split the sentence into words
    for i in range(1, len(words), 2):  # start from the second word and iterate every second word
        words[i] = words[i][::-1]  # flip (reverse) the word
    return ' '.join(words)  # join the words back into a sentence