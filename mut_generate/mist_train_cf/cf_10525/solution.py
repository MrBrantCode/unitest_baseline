"""
QUESTION:
Write a function called `find_second_largest` that takes an array of integers as input and returns the second largest number in the array. The function should not use any built-in sorting functions or additional data structures, and it should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_second_largest(nums):
    largest = float('-inf')
    secondLargest = float('-inf')
    
    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num
    
    return secondLargest