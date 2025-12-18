"""
QUESTION:
Write a function `find_longest_word_length(sentence)` that takes a string `sentence` as input and returns the length of the longest word in the sentence without using any built-in string manipulation functions or methods. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the sentence.
"""

def find_longest_word_length(sentence):
    max_length = 0
    current_length = 0

    for char in sentence:
        if char != ' ':
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0

    # Check the last word
    return max(max_length, current_length)