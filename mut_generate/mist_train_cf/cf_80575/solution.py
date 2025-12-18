"""
QUESTION:
Given an array `nums` of positive integers, return the count of unique GCDs among all non-empty subsequences of `nums`. 

The array `nums` contains `n` integers where `1 <= n <= 10^5` and each integer `nums[i]` satisfies `1 <= nums[i] <= 2 * 10^5`.
"""

def countDifferentSubsequenceGCDs(nums):
    max_num = max(nums)
    freq = [0] * (max_num + 1)
    
    for num in nums:
        freq[num] += 1
        
    count = 0
    for i in range(max_num, 0, -1):
        if freq[i] > 0:
            count += 1
        else:
            for j in range(2*i, max_num + 1, i):
                if freq[j] > 0:
                    freq[i] = 1
                    break
            if freq[i] > 0:
                count += 1
    return count