"""
QUESTION:
Find the missing numbers in an unsorted array of unique integers from 1 to n, without using extra space and with a time complexity of O(n). The function should take an array of integers as input and return a list of missing numbers. The function is allowed to modify the input array. The array index starts at 0, but the numbers in the array and the missing numbers are 1-indexed.
"""

def find_missing_numbers(nums):
    n = len(nums)

    # mark elements as negative using index as a hash key 
    for i in range(n): 
        num = abs(nums[i]) - 1
        if num < n:
            nums[num] = -abs(nums[num])

    # now the index of the positive numbers are the missing elements
    missing = [i+1 for i in range(n) if nums[i] > 0]

    return missing