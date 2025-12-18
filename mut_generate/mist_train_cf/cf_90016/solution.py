"""
QUESTION:
Find the three highest distinct numbers in an array of integers in descending order. The input array will contain at most 10^5 integers, ranging from -10^9 to 10^9. The algorithm should have a time complexity of O(n) and use constant space, and should not modify the original array. 

Implement the function `find_3_highest_distinct_numbers(nums)` to solve this problem.
"""

def find_3_highest_distinct_numbers(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    distinct_nums = list(count.keys())
    distinct_nums.sort(reverse=True)
    
    return distinct_nums[:3]