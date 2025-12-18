"""
QUESTION:
You are given array nums of n length and an integer k .return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example:
Input:
n = 11
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
Output:
6
Explanation:
You can flip 2 0 and obtain  [1,1,1,0,0,1,1,1,1,1,1]
Your Task:
You don't have to read input or print anything. Your task is to complete the function longestOnes() which takes the integer n and array nums and integer K as input and returns the longest ones which can be obtained after k flip.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
Constraint:
1<=n<=10^{5}
0<=nums<=1
0<=k<=n
"""

def longest_ones(nums: list[int], k: int) -> int:
    left = 0
    right = 0
    zero_count = 0
    maxlen = 0
    
    while right < len(nums):
        if nums[right] == 1:
            right += 1
        elif zero_count < k:
            zero_count += 1
            right += 1
        else:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        maxlen = max(maxlen, right - left)
    
    return maxlen