"""
QUESTION:
Write a function `find_largest_second_largest` that takes a list of integers as input and returns the largest and second largest numbers in the list. The function should have a time complexity of O(n), where n is the number of elements in the list, and should not use any built-in sorting functions or libraries. The input list can contain duplicates and can have up to 10^6 elements.
"""

def find_largest_second_largest(nums):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return largest, second_largest