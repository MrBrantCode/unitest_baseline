"""
QUESTION:
Implement a function named "recursive_linear_search" that takes a list of numbers and a target number as parameters, and returns the position of the target number in the list. The function should have a time complexity of O(n) and utilize a recursive approach. If the target number is not found, return -1.
"""

def recursive_linear_search(numbers, target):
    def search(numbers, target, index):
        if index == len(numbers):
            return -1
        if numbers[index] == target:
            return index
        return search(numbers, target, index + 1)
    
    return search(numbers, target, 0)