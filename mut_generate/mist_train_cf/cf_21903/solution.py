"""
QUESTION:
Write a function `find_second_largest` that takes a list of integers as input and returns the second largest element. If there is no second largest element (i.e., the list has less than two distinct elements), the function should return None. The function should handle duplicate values, negative integers, and empty lists correctly, and have a time complexity of O(n), where n is the length of the list.
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