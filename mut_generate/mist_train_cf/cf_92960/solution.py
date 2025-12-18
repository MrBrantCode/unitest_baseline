"""
QUESTION:
Write a function `reverse_words` that takes a string as input, reverses the order of words, and reverses each word itself, then returns the resulting string. The input string can contain punctuation and spaces. The function should not use any external libraries or modules.
"""

def reverse_words(string):
    words = string.split()  # Split the string into an array of words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = ' '.join(reversed_words[::-1])  # Join the reversed words into a single string
    return reversed_string