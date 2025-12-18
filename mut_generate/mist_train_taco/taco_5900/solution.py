"""
QUESTION:
You have d dice, and each die has f faces numbered 1, 2, ..., f.
Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.
 
Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:
Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.

 
Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""

from math import comb

def num_rolls_to_target(d: int, f: int, target: int) -> int:
    MOD = 1000000007
    
    if target < d or target > d * f:
        return 0
    
    target = target - d
    sum_ways = 0
    i = 0
    j = 0
    
    while i <= target:
        y = target - i
        if j % 2 == 0:
            sum_ways = (sum_ways + comb(d, j) * comb(y + d - 1, y)) % MOD
        else:
            sum_ways = (sum_ways - comb(d, j) * comb(y + d - 1, y)) % MOD
        j += 1
        i += f
    
    return sum_ways