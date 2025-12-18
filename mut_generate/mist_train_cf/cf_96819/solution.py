"""
QUESTION:
Create a function named `find_second_largest` that takes a list of integers as input and returns the second largest element in the list. The function should have a time complexity of O(n), where n is the length of the list. The function should handle lists with duplicate values, negative integers, empty lists, and lists with only one element correctly, returning None if there is no second largest element in the list.
"""

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = arr[0]
    second_largest = None
    
    for num in arr[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    
    return second_largest