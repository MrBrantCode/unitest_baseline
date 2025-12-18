"""
QUESTION:
Create a function `find_two_largest` that takes a list of integers and returns the two largest numbers in the list. The function should have a time complexity of O(n), not use any built-in sorting functions, and only iterate through the list once without modifying the original list. It should handle cases with negative numbers, duplicate numbers, and lists with less than 2 elements, returning an error message in the latter case.
"""

def find_two_largest(numbers):
    if len(numbers) < 2:
        return "Error: List must have at least two elements."
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    return largest, second_largest