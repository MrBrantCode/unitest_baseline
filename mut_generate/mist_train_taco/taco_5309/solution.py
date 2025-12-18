"""
QUESTION:
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.



Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].



Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

def can_partition(nums: list[int]) -> bool:
    _sum = sum(nums)
    div, mod = divmod(_sum, 2)
    if mod != 0:
        return False
    
    target = [div] * 2
    nums.sort(reverse=True)
    _len = len(nums)
    
    def dfs(index: int, target: list[int]) -> bool:
        if index == _len:
            return True
        num = nums[index]
        for i in range(2):
            if target[i] >= num:
                target[i] -= num
                if dfs(index + 1, target):
                    return True
                target[i] += num
        return False
    
    return dfs(0, target)