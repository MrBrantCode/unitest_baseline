"""
QUESTION:
Design a function named `multiply_list` that computes the multiplication of a list of numbers. The input list will only contain positive integers and its length can be up to 10^6. The function should have a time complexity of O(n).
"""

def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result