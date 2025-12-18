"""
QUESTION:
Write a function sum_triple that takes three numbers as input and returns their sum, with two conditions: 
- If all three values are equal, then return triple their sum.
- If any two values are equal but the third one is not, return the square of the sum.
- If none of the above conditions are met, return the sum of the numbers.
Assume input is a list or other iterable of three numbers.
"""

def sum_triple(numbers): 
    if len(set(numbers)) == 1:
        return sum(numbers) * 3
    elif len(set(numbers)) == 2:
        return sum(numbers) ** 2
    else:
        return sum(numbers)