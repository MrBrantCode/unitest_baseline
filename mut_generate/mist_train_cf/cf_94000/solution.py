"""
QUESTION:
Write a function called `find_smallest_number` that takes an array of numbers as input and returns the smallest number in the array. The function must not use any conditional statements (such as if/else or switch) or built-in functions that directly solve this problem. The time complexity of the function should be O(n) and the space complexity should be O(1), where n is the length of the input array.
"""

def find_smallest_number(numbers):
    smallest = numbers[0]
    for num in numbers[1:]:
        smallest = num if num < smallest else smallest
    return smallest