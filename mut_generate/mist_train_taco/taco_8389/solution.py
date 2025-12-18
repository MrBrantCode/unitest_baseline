"""
QUESTION:
In a town , the Chief Council of Ministers has decided to contribute funds raised from various sources in their department for the Central Public Welfare Initiatives. Given the contribution of n ministers nums_{i}, where i represents the contribution of the i^{th} minister, what should be the least contribution from the chief such that the n^{th} power of his share is atleast equal to the product of contributions of all his subordinates.
Example 1:
Input: nums = {3, 2, 1, 5}
Output: 3
Explanation: 3^{4} >= 3*2*1*5 = 30
Example 2:
Input: nums = {2}
Output: 2
Explanation: 2^{1} >= 2
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Find() which takes list nums as input parameter and returns the minimum contribution such that it's n^{th} power is atleast equal to the product of contributions of all sunordinates of Chief.
Expected Time Complexity: O(nlog(n))
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 10000
1 <= nums_{i} <= 100
"""

import math

def find_min_chief_contribution(nums):
    total = 0
    n = len(nums)
    for a in nums:
        total += math.log(a)
    total /= n
    x = math.exp(total)
    return math.ceil(x)