"""
QUESTION:
Implement a function named `reverse_words_string` that takes a string as input, reverses each word in the string, and returns the resulting string. The function should not use Python's built-in reverse functions or slicing techniques.
"""

def reverse_words_string(string):
    n = len(string)
    word = ""
    stack = []

    for i in range(n):
        if string[i] != ' ':
            word += string[i]
        else:
            stack.append(word)
            word = ""

    stack.append(word)
    out_string = ""

    while len(stack) != 0:
        pop_word = stack.pop()
        for i in range(len(pop_word)-1, -1, -1):
            out_string += pop_word[i]
        if len(stack) != 0:
            out_string += ' '

    return out_string