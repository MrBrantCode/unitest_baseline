"""
QUESTION:
Write a function `find_smallest_number` that takes an array of numbers as input and returns the smallest number in the array. The function should have a time complexity of O(n), where n is the number of elements in the array, and should not use any built-in functions, additional data structures, recursion, or conditional statements beyond a simple loop. The function should handle arrays with negative numbers, duplicate numbers, large arrays, and floating-point numbers, and should not modify the original array.
"""

def find_smallest_number(numbers):
    if len(numbers) == 0:
        return None
    
    smallest = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    
    return smallest