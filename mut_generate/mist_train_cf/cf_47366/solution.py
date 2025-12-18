"""
QUESTION:
Create a function named `eliminate_words` that takes an array of strings (`arr`) and a single character (`letter`) as input. The function should return a new array containing only the words from `arr` that do not contain the specified `letter`.
"""

def eliminate_words(arr, letter):
    return [word for word in arr if letter not in word]