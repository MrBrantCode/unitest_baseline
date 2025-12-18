"""
QUESTION:
Write a function called `calculate_sum` that takes a list of numbers as input and returns the sum of all the numbers in the list. Implement the function with a time complexity of O(n) and a space complexity of O(1), without using the built-in sum() function or any other function that directly calculates the sum of a list.
"""

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total