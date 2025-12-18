"""
QUESTION:
Write a function named `multiply_by_two` that takes a list of integers as input and returns a new list where each number in the input list is multiplied by 2, while maintaining the original order.
"""

def multiply_by_two(numbers):
    results = []
    for number in numbers:
        results.append(number * 2)
    return results