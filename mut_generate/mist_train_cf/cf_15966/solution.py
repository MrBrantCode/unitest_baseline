"""
QUESTION:
Write a function `find_smallest_number` that takes an array of numbers as input and returns the smallest number in the array. The function must not use conditional statements (if/else, switch) or built-in functions that directly solve the problem (min(), Math.min()). The time complexity must be O(n) and space complexity must be O(1), where n is the length of the input array.
"""

def find_smallest_number(numbers):
    smallest = numbers[0]
    for num in numbers[1:]:
        smallest = num if num < smallest else smallest
    return smallest