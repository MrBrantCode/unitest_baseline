"""
QUESTION:
Implement a function called "recursive_linear_search" that takes in a list of numbers and a target number as parameters. The function should utilize a recursive approach to search for the target number in the list and return its position. The function should have a time complexity of O(n) and return -1 if the target number is not found.
"""

def recursive_linear_search(numbers, target):
    def search(numbers, target, index):
        if index == len(numbers):
            return -1
        if numbers[index] == target:
            return index
        return search(numbers, target, index + 1)
    
    return search(numbers, target, 0)