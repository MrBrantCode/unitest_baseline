"""
QUESTION:
Write a function `find_second_largest` that takes a list of positive integers as input. The list must have at least 5 elements, cannot contain duplicates, and can have up to 1000 elements. The function should return the second largest element in the list. If the list has less than 5 elements, the function should return `None`.
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