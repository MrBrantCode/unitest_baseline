"""
QUESTION:
Create a function `find_unique_number` that takes a list of integers as input. The function should return a single unique number from the list using only bitwise operations and without using any arithmetic or comparison operators. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_unique_number(numbers):
    unique_num = 0
    for num in numbers:
        unique_num ^= num
    return unique_num