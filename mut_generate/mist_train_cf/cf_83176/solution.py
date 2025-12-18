"""
QUESTION:
Create a function called `binary_search` that performs a binary search on a sorted list of integers and returns the position of the target integer and the number of steps it took to find it. The function should take two parameters: a sorted list of integers `nums` and the target integer `target`. The function should return a tuple containing the position of the target integer in the list and the number of steps taken, or `(None, steps)` if the target integer is not found.
"""

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == target:
            return mid, steps
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None, steps