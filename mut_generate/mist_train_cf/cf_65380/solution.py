"""
QUESTION:
Implement a function named `final_result` that takes an array `nums` and an integer `k` as input, where `1 <= len(nums) <= 2 * 10^4` and `0 <= k <= 10^5`. The function should rotate `nums` to the right by `k` steps, calculate the sum of all the elements at even indices, subtract the sum of all the elements at odd indices, and return the result. The rotation should be done in-place and the extra space complexity should be `O(1)`.
"""

def final_result(nums, k):
    n = len(nums)
    k %= n
    
    def reverse(start, end):
        i, j = start, end - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    reverse(0, n)
    reverse(0, k)
    reverse(k, n)
    
    even_sum, odd_sum = sum(nums[i] for i in range(0, n, 2)), sum(nums[i] for i in range(1, n, 2))
    
    return even_sum - odd_sum