"""
QUESTION:
Write a function called `find_longest_words` that takes a list of strings as input and returns a list of the longest words. If there are multiple words with the same maximum length, the function should return all of them. You must implement your own algorithm to find the longest words without using the built-in `max()` function or any other built-in functions that directly solve the problem.
"""

def find_longest_words(words):
    longest_words = []
    max_length = 0

    for word in words:
        length = len(word)
        if length > max_length:
            longest_words = [word]
            max_length = length
        elif length == max_length:
            longest_words.append(word)

    return longest_words