"""
QUESTION:
Implement a function `remove_duplicates` that takes a string of lowercase alphabets separated by spaces as input and returns a string with all duplicated words removed. The length of the string will not exceed 10000 characters and the solution should have a time complexity of O(n), where n is the length of the string.
"""

def remove_duplicates(input_string):
    words = input_string.split()
    unique_words = set()
    for word in words:
        unique_words.add(word)
    return ' '.join(unique_words)