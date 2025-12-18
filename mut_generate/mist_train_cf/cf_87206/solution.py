"""
QUESTION:
Create a function named `filter_divisible_by_3_and_7` that takes an array of positive integers as input and returns a new array containing unique elements that are divisible by both 3 and 7, sorted in ascending order. The function should not use any built-in functions for sorting or removing duplicates and should have a time complexity of O(n), where n is the length of the input array.
"""

def entrance(arr):
    # Step 1: Find all elements divisible by both 3 and 7
    divisible_elements = []
    for num in arr:
        if num % 3 == 0 and num % 7 == 0:
            divisible_elements.append(num)
    
    # Step 2: Remove duplicates and sort the array
    unique_elements = []
    for num in divisible_elements:
        if num not in unique_elements:
            unique_elements.append(num)
    unique_elements.sort()
    
    return unique_elements