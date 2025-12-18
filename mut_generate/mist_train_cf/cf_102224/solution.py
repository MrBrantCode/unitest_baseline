"""
QUESTION:
Write a function named `count_hello` that takes a list of words as input and returns the total count of the word "hello" in the list. The list can be of any length and may contain duplicate words.
"""

def count_hello(words):
    count = 0
    for word in words:
        if word == "hello":
            count += 1
    return count