"""
QUESTION:
Implement a function `sum_of_unique_pairs(nums, target)` that takes a list of integers `nums` and a target value `target` as input and returns the sum of all unique pairs of numbers in `nums` that add up to `target`. The function should have a time complexity of O(n), where n is the length of `nums`, and should handle duplicate values, negative and large numbers, and edge cases such as an empty list.
"""

def sum_of_unique_pairs(nums, target):
    if not nums:  # Handle empty list
        return 0

    seen = set()  # Set to store unique pairs
    pair_sum = 0  # Variable to store the sum of unique pairs

    for num in nums:
        complement = target - num  # Calculate the complement for each number

        if complement in seen:  # Check if complement exists in the set
            pair_sum += num + complement  # Add the pair sum to the total sum

        seen.add(num)  # Add the number to the set

    return pair_sum