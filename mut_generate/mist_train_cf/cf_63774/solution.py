"""
QUESTION:
Write a function named `reverse_words` that takes a sentence as input, reverses each word individually, and returns the modified sentence without reversing the order of the words or using any built-in functions or methods.
"""

def reverse_words(sentence):
    result = ""
    word = ""
    for char in sentence:
        if char == " ":
            result = result + word[::-1] + " "
            word = ""
        else:
            word += char
    return result + word[::-1]