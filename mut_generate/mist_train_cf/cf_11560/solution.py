"""
QUESTION:
Write a function `find_second_largest` that takes a list of numbers as input and returns the second largest element in the list. If the list has less than two elements, the function should return `None`. The function should have a time complexity of O(n).
"""

def entance(numbers):
    if len(numbers) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest