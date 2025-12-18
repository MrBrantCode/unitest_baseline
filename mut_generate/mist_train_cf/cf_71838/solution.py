"""
QUESTION:
Write a function called `function` that takes a string as input, reverses the order of words, and also reverses the order of characters within each word. The function should not use any built-in Python functions or libraries for reversing strings. 

For example, `function("Hello World!")` should return `!dlroW olleH` and `function("Python Programming is Fun")` should return `nuF si gnimmargorP nohtyP`.
"""

def reverse_string(s):
    words = s.split(' ')
    result = ""
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        result = reversed_word + ' ' + result
    return result[:-1]  # Remove the extra space at the end