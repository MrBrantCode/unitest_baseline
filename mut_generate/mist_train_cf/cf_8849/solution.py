"""
QUESTION:
Design a function called `multiply_list` that takes a list of positive integers as input and returns their product. The input list can be up to 10^6 elements long, and the function should have a time complexity of O(n).
"""

def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result