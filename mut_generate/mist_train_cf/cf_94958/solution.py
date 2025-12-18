"""
QUESTION:
Write a function `find_longest_word` that takes an array of strings as input and returns the word with the maximum length. The function should not use any built-in functions or methods that directly solve the problem. The input array is guaranteed to be non-empty and contain only strings.
"""

def find_longest_word(arr):
    max_length = 0
    longest_word = ""
    
    for word in arr:
        length = 0
        for char in word:
            length += 1
        if length > max_length:
            max_length = length
            longest_word = word
    
    return longest_word