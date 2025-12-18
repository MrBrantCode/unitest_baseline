"""
QUESTION:
Create a function named `last_two_elements` that takes one parameter (an array containing any data types). This function should return the last two elements of the given array without using any built-in or library functions.
"""

def last_two_elements(myArray):
    lastElement = myArray[-1]
    secondLastElement = myArray[-2]

    return secondLastElement, lastElement