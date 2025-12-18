"""
QUESTION:
Write a function named `find_second_largest` that takes a list of distinct positive integers as input and returns the second largest number. The input list must have at least 5 elements and the function should be able to handle lists with up to 1000 elements efficiently.
"""

def find_second_largest(numbers):
    if len(numbers) < 5:
        return None
    
    largest = numbers[0]
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest