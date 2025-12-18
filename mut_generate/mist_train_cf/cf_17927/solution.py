"""
QUESTION:
Implement a function named `find_longest_word` that takes an array of strings as input. The function should find the total length of all words in the array and return the word with the maximum length without using any built-in functions or methods that directly solve the problem.
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