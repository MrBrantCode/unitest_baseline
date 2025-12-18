"""
QUESTION:
Implement a function `sum_multiples` that takes an array of integers and an integer 'n'. The function should return the sum of all unique elements in the array that are multiples of 'n'. If 'n' is 0, the function should return an error message, as division by zero is undefined.
"""

def sum_multiples(array, n):
    if n==0:
        return "Error: 'n' must not be zero."
    else:
        return sum(set(x for x in array if x % n == 0))