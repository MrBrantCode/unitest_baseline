"""
QUESTION:
Implement a function `count_pairs(nums, k)` that counts the number of non-consecutive pairs in a list `nums` whose difference is `k`. The function should achieve a time complexity of O(n log n). The list `nums` contains integers, and `k` is an integer.
"""

def count_pairs(nums, k):
    nums.sort()
    count = 0
    left, right = 0, 1

    while right < len(nums): 
        if nums[right] - nums[left] == k: 
            count += 1
            left += 1
            right += 1
        elif nums[right] - nums[left] > k:  
            left += 1  
        else:  
            right += 1  
            
    return count