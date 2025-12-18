"""
QUESTION:
Write a function `reverse_words(sentence)` that takes a string `sentence` containing only letters and spaces as input, reverses the words in place without using any additional data structures or built-in string manipulation functions, and returns the reversed sentence. Ensure the solution has a time complexity of O(n), where n is the length of the sentence.
"""

def reverse_words(sentence):
    sentence = list(sentence)

    start = 0
    end = 0

    while end < len(sentence):
        if sentence[end] == ' ':
            reverse_word(sentence, start, end - 1)
            start = end + 1
        end += 1

    reverse_word(sentence, start, end - 1)
    sentence = ''.join(sentence)
    
    return sentence


def reverse_word(sentence, start, end):
    while start < end:
        sentence[start], sentence[end] = sentence[end], sentence[start]
        start += 1
        end -= 1