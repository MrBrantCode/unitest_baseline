"""
QUESTION:
Given an array where each element is the money a person have and there is only Rs. 3 note. We need to check whether it is possible to divide the money equally among all the persons or not. If it is possible then find Minimum number of transactions needed.
 
Example 1:
Input: nums = [5, 8, 11]
Output: 1
Explanation: 3rd person can give Rs. 3
then all person would have Rs. 8
Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 1 + 2 + 3 + 4 = 10. Rs. 10 
can not be distributed among 4 persons.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function MinimumTransaction() which takes the array as input parameter and returns the minimum number of transactions needed to distribute the money equally. If not possible returns -1.
 
Expected Time Complexity: O(n) where n is length of array
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 10^{5}
1 <= elements of array <= 10^{6}
"""

def minimum_transactions(nums):
    s = sum(nums)
    if s % len(nums) != 0:
        return -1
    m = s // len(nums)
    res = 0
    for i in range(len(nums)):
        diff = nums[i] - m
        if diff <= 0:
            continue
        if diff % 3 != 0:
            return -1
        res += diff // 3
    return res