"""
QUESTION:
Implement a function `reverse_words(sentence)` that takes a list of characters representing a sentence as input and reverses the characters in each word without using any built-in string manipulation functions or libraries and only constant extra space. The function should return the list of characters with the words reversed.
"""

def reverse_words(sentence):
    start = 0
    for end in range(len(sentence) + 1):
        if end == len(sentence) or sentence[end] == ' ':
            left, right = start, end - 1
            while left < right:
                sentence[left], sentence[right] = sentence[right], sentence[left]
                left, right = left + 1, right - 1
            start = end + 1
    return sentence