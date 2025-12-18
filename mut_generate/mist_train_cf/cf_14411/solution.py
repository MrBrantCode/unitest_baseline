"""
QUESTION:
Write a function named `reverse_characters` that takes an array of strings as input and returns a new array where each string is reversed character by character, without using any built-in string reversal functions or methods.
"""

def reverse_characters(array):
    reversed_array = []
    for word in array:
        reversed_word = ''
        for char in word:
            reversed_word = char + reversed_word
        reversed_array.append(reversed_word)
    return reversed_array