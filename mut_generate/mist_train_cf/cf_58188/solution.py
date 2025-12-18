"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list of numbers (`numbers`) and a target number (`target`) as input. The list can contain integers, floating point numbers with up to ten decimal places, and repetitions. The function should return the index of the first occurrence of the target element if found, otherwise return -1. The solution should aim for optimized time and space complexity, handling corner cases like an empty list or a list with only one element, and be efficient for lists containing up to 1 million numbers.
"""

def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            # If target is found, move left pointer towards mid to find first occurrence 
            while mid != 0 and numbers[mid-1] == target:
                mid -= 1
            return mid

        elif target < numbers[mid]:
            right = mid - 1

        else: # target > numbers[mid]
            left = mid + 1

    return -1