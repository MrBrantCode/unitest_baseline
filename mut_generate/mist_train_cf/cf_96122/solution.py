"""
QUESTION:
Write a function `repeat_elements(alphabet)` that takes an array of strings as input and returns a new array where each string is repeated a number of times equal to its length. Do not use built-in methods or functions to repeat the elements. The function should handle empty strings, arrays with multiple elements of the same length, and potential errors or exceptions that may occur during execution.
"""

def repeat_elements(alphabet):
    repeated_alphabet = []
    for word in alphabet:
        repeated_word = ""
        for i in range(len(word)):
            repeated_word += word
        repeated_alphabet.append(repeated_word)
    return repeated_alphabet