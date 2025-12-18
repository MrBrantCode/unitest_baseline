"""
QUESTION:
Write a function `merge_de_dupe_and_count_pairs` that takes two sorted arrays of integers and a target integer as input, merges the arrays into one sorted array without duplicates, and returns the merged array along with the number of pairs of numbers that add up to the target.
"""

def merge_de_dupe_and_count_pairs(arr1, arr2, target):
    # Merge arrays
    merged = sorted(set(arr1 + arr2))
    
    # Initialize two pointers at both ends
    left, right = 0, len(merged) - 1
    count = 0
    
    while left < right:
        curr_sum = merged[left] + merged[right]

        # If current sum is less than target, increment left pointer
        if curr_sum < target:
            left += 1
        # If current sum is more than target, decrement right pointer
        elif curr_sum > target:
            right -= 1
        # If current sum is equal to target, increment count and move both pointers
        else:
            count += 1
            left += 1
            right -= 1
            
    return merged, count