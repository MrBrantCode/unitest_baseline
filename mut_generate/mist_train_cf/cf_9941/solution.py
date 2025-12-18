"""
QUESTION:
Write a function `reverse_print(text)` that takes a string `text` as input and prints the characters of the string in reverse order without using any built-in string reversal function or loop. The function should have a time complexity of O(n), where n is the length of `text`, and should not use any additional data structures.
"""

def reverse_print(text):
    if len(text) == 0:
        return
    else:
        reverse_print(text[1:])
        print(text[0], end='')