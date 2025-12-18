"""
QUESTION:
Write a function `find_longest_word` that takes an array of strings as input. Using a single loop, find the total length of all words in the array and the word with the maximum length. Do not use any built-in functions or methods that directly solve the problem. The function should return the word with the maximum length and the total length of all words.
"""

def find_longest_word(arr):
    total_length = 0
    longest_word = ""

    for word in arr:
        length = 0
        for char in word:
            length += 1
        total_length += length

        if length > len(longest_word):
            longest_word = word

    return longest_word, total_length