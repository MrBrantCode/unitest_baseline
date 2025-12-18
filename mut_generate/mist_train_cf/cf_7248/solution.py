"""
QUESTION:
Implement a function `calculate_sum` that calculates the sum of all numbers in a given list, without using the built-in sum() function or any other function that directly calculates the sum of a list. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total