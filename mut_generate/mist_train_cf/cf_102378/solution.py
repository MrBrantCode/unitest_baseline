"""
QUESTION:
Write a function `squareNumbers` that takes an array of numbers as input and returns an object where the keys are the numbers from the array and the values are their squares. Implement the function using JavaScript, utilizing arrow functions and avoiding the use of "for...in" loops.
"""

def squareNumbers(numbers):
    squared = {}
    for num in numbers:
        squared[num] = num ** 2
    return squared