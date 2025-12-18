"""
QUESTION:
Write a function `find_second_largest` that takes a list of integers as input and returns the second largest number and its frequency. If there are multiple numbers with the same frequency, return the smallest number among them. If no second largest number exists, return None.
"""

def find_second_largest(nums):
    largest = float('-inf')
    secondLargest = float('-inf')
    largestFreq = 0
    secondLargestFreq = 0

    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
            secondLargestFreq = largestFreq
            largestFreq = 1
        elif num == largest:
            largestFreq += 1
        elif num > secondLargest and num != largest:
            secondLargest = num
            secondLargestFreq = 1
        elif num == secondLargest:
            secondLargestFreq += 1

    if secondLargest == float('-inf'):
        return None

    return (secondLargest, secondLargestFreq)