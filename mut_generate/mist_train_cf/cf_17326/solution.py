"""
QUESTION:
Create a function called `find_two_largest` that takes a list of integers as input and returns the two largest numbers in the list. The function should have a time complexity of O(n) and not use any built-in sorting functions or additional data structures. It should iterate through the list only once and not modify the original list. If the input list has less than 2 elements, the function should return an error message.
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
        elif num > second_largest and num != largest:
            second_largest = num
    
    return largest, second_largest