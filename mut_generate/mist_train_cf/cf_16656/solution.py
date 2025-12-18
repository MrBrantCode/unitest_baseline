"""
QUESTION:
Create a function `find_unique_number` that takes a list of numbers as input and returns a single unique number. The function should have a time complexity of O(n) and a space complexity of O(1), and it must only use bitwise operations, excluding arithmetic and comparison operators.
"""

def find_unique_number(numbers):
    unique_num = 0
    for num in numbers:
        unique_num ^= num
    return unique_num