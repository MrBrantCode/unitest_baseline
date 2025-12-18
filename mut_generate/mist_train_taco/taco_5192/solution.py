"""
QUESTION:
Given an array nums[] of n elements and a number k. Your task is to count the number of integers from 1 to k which are divisible by atleast one of the elements of nums[].
 
Example 1:
Input: nums = {2, 3}, k = 10
Output: 7
Explanation: The numbers from 1 to 10
which are divisible by either 2 or 3
are - 2, 3, 4, 6, 8, 9, 10
Example 2:
Input: nums = {2}, k = 5
Output: 2
Explanation: The numbers which are divisble 
by 2 from 1 to 5 are 2 and 4.
 
Your Task:
You don't have to read or print anyhting. Your task is to complete the function Count() which takes nums and k as input parameter and returns count of integers from 1 to k which are divisible by atleast one of the element of nums[].
 
Expected Time Compelxity: O(n * 2^{n} * log(k))
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 12
1 <= k <= 10^{18}
1 <= nums[i] <= 20
"""

import math

def count_divisible_numbers(nums, k):
    ans = 0
    n = len(nums)
    for i in range(1, 1 << n):
        cnt = 0
        val = 1
        for j in range(n):
            if i & 1 << j:
                cnt += 1
                val = val * nums[j] // math.gcd(val, nums[j])
        sign = 1 if cnt % 2 else -1
        ans += sign * (k // val)
    return ans