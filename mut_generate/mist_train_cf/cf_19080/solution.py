"""
QUESTION:
Create a function called `insertAtBeginning` that takes an array and an element as input and returns a new array with the element inserted at the beginning, without using built-in array methods such as `unshift` or `splice`.
"""

def insertAtBeginning(array, element):
    return [element] + array