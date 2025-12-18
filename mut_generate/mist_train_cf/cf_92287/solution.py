"""
QUESTION:
Create a function named `find_long_words` that takes a string as input and returns a list of words that have more than 7 characters. The input string contains multiple words separated by spaces and may include punctuation marks.
"""

def find_long_words(input_string):
    words = input_string.split()  # Split the string into words
    long_words = [word for word in words if len(word) > 7]  # List comprehension to filter long words
    return long_words