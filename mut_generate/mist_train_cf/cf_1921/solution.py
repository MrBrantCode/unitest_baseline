"""
QUESTION:
Write a function called `filter_divisible_by_3_and_7` that takes an array of positive integers as input and returns a new array containing all elements that are divisible by both 3 and 7, without any duplicates, and in ascending order. The function should have a time complexity of O(n), where n is the length of the input array, and should not use any built-in functions for sorting or removing duplicates.
"""

def filter_divisible_by_3_and_7(arr):
    # Step 1: Find all elements divisible by both 3 and 7
    divisible_elements = set()
    for num in arr:
        if num % 3 == 0 and num % 7 == 0:
            divisible_elements.add(num)
    
    # Step 2: Convert set back to list and sort the array
    result = list(divisible_elements)
    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result