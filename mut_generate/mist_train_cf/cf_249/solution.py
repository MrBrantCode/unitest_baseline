"""
QUESTION:
Write a function `find_second_largest(lst)` that takes a list of integers as input and returns the second largest value in the list. The function should not use any built-in sorting functions or libraries. The time complexity should be O(n), where n is the length of the list, and the space complexity should be O(1). If the list has less than two elements, the function should return `None`.
"""

def find_second_largest(lst):
    if len(lst) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    
    return second_largest