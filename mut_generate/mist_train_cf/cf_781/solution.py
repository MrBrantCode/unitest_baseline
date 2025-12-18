"""
QUESTION:
Write a recursive function `findMin` that takes a list of numbers as input and returns the minimum value without using loops or helper functions. The function should have a maximum time complexity of O(n^2), where n is the length of the input list, and should not exceed 10 levels of recursive calls.
"""

def findMin(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
        min_left = findMin(left)
        min_right = findMin(right)
        return min(min_left, min_right)