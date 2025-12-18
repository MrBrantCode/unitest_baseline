"""
QUESTION:
Implement a function called `findMin` that calculates the minimum value in a given list of numbers using a recursive algorithm without any loops or helper functions, with a maximum time complexity of O(n^2).
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