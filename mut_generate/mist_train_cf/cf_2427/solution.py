"""
QUESTION:
Create a function named `find_two_largest` that takes a list of integers as input and returns the two largest numbers in the list. The function should have a time complexity of O(n), iterate through the list only once, and not use any built-in sorting functions, max or min functions, or additional data structures. If the input list contains less than two numbers, the function should return an error message. The function should handle cases with negative numbers, duplicate numbers, and return a tuple containing the two largest numbers.
"""

def find_two_largest(numbers):
    if len(numbers) < 2:
        return "Error: Input list must contain at least two numbers."
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return (largest, second_largest)