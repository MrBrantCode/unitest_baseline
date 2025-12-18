"""
QUESTION:
Write a function named `fill_dictionary` that takes an integer `n` as input and returns a dictionary where the keys are numbers from 1 to `n` and the values are their corresponding squares as strings.
"""

def fill_dictionary(n):
    dictionary = {}
    for num in range(1, n+1):
        dictionary[num] = str(num ** 2)
    return dictionary