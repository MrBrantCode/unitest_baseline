"""
QUESTION:
Write a function `find_3_highest_distinct_numbers(nums)` that takes an array of integers `nums` as input and returns the 3 highest distinct numbers in descending order. The function should have a time complexity of O(n), use constant space, and not modify the original array. The input array will contain at most 10^5 integers, ranging from -10^9 to 10^9.
"""

def find_3_highest_distinct_numbers(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    distinct_nums = list(count.keys())
    distinct_nums.sort(reverse=True)
    
    return distinct_nums[:3]