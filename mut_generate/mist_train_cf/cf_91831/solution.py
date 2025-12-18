"""
QUESTION:
Write a function named `replace_kth_smallest` that takes an integer array `nums` and an integer `K` as inputs. The function should replace the Kth smallest number in the array with 0 and return the modified array. The function must have a time complexity of O(n log n) and a space complexity of O(1).
"""

def replace_kth_smallest(nums, K):
    # Sort the array in ascending order
    nums.sort()
    
    # Replace the Kth smallest number with 0
    nums[K-1] = 0
    
    return nums