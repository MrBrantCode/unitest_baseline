"""
QUESTION:
Create a function `find_word` that takes in a list of words and a target word. The function should return the original word from the list if the target word matches the original word or its reverse. If no match is found, return None.
"""

def find_word(words, target):
    for word in words:
        if word == target or word == target[::-1]:
            return word
    return None