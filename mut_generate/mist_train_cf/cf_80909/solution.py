"""
QUESTION:
Write a function `binary_search` that takes an unsorted list of numbers and a target number as input, and returns the index of the first occurrence of the target number in the sorted list. If the target number is not found, return "Not found". The function should be able to handle duplicate entries in the list. The input list is not guaranteed to be sorted.
"""

def binary_search(numbers, target):
    numbers.sort()  # sorts the list in ascending order

    first = 0
    last = len(numbers) - 1

    while first <= last:
        mid = (first + last) // 2

        if numbers[mid] == target : 
            # If numbers[mid] equals target, we found a match
            # However, we need to check if there are duplicates to the left
            while mid > 0 and numbers[mid-1] == target:
                mid -= 1
            return mid

        # If target is smaller than numbers[mid], it can only be in the left subarray
        elif target < numbers[mid]:
            last = mid -1

        # Otherwise, the target can only be in the right subarray
        else:
            first = mid + 1

    # If the number has not been found
    return "Not found"