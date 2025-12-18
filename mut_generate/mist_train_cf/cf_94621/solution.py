"""
QUESTION:
Write a function `findThirdLargest(nums)` that takes an array of integers `nums` as input and returns the third largest number in the array. The function should have a time complexity of O(n) and a space complexity of O(1), without using any built-in sorting functions or additional data structures.
"""

def entrance(nums):
    largest = float('-inf')
    secondLargest = float('-inf')
    thirdLargest = float('-inf')

    for num in nums:
        if num > largest:
            thirdLargest = secondLargest
            secondLargest = largest
            largest = num
        elif secondLargest < num < largest:
            thirdLargest = secondLargest
            secondLargest = num
        elif thirdLargest < num < secondLargest:
            thirdLargest = num

    return thirdLargest