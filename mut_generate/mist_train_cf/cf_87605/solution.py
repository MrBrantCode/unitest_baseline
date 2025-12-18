"""
QUESTION:
Create a function named `process_list` that takes a list of integers as input. The function should return a new list containing the squares of the input elements that are divisible by 2 but not by 3. The resulting list should be sorted in descending order.
"""

def process_list(numbers):
    result = sorted([x ** 2 for x in numbers if x % 2 == 0 and x % 3 != 0], reverse=True)
    return result