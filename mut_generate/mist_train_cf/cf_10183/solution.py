"""
QUESTION:
Write a function `divisible_by_two(numbers)` that takes a list of integers `numbers` as input and returns a list of boolean values indicating whether each number is divisible by 2. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def divisible_by_two(numbers): 
    result = [num % 2 == 0 for num in numbers]
    return result