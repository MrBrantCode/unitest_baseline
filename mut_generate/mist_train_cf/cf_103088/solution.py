"""
QUESTION:
Write a function named `odd_numbers` that takes a list of integers as input, and returns a new list containing only the odd numbers from the input list. Do not use any built-in functions or libraries.
"""

def odd_numbers(lst):
    output = []
    for num in lst:
        if num % 2 != 0:
            output.append(num)
    return output