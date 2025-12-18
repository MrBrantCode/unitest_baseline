"""
QUESTION:
Create a function `find_divisible` that takes a list of integers `nums` as input, removes duplicates, and returns a list of numbers that are divisible by 3 in ascending order. The function should not use built-in sorting or duplicate removal functions, have a time complexity of O(n), use constant extra space, and not modify the input list. It should also handle negative numbers correctly.
"""

def find_divisible(nums):
    # Remove duplicates and store unique elements in a dictionary for O(1) lookup
    unique_nums = {}
    for num in nums:
        unique_nums[num] = True

    # Initialize the result list
    result = []

    # Iterate through the unique numbers and check if they are divisible by 3
    for num in unique_nums:
        if num % 3 == 0:
            # Add the number to the result list
            result.append(num)

    # Sort the result list in ascending order
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    # Return the result list
    return result