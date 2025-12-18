"""
QUESTION:
Write a function named `greater_than_target` that takes two parameters: a list of integers and a target integer. Return a new list containing only the elements from the original list that are greater than the target integer.
"""

def greater_than_target(numbers, target):
    result = []
    for num in numbers:
        if num > target:
            result.append(num)
    return result