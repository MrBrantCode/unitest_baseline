"""
QUESTION:
An enemy spy has poisoned one out of N sweets in a bakery. Even a bite of the poisoned sweet has potency to kill. However, the effects of the poison show only in 30 days. The managers asks the jailor to identify the poisoned sweet within 30 days. What is the least number of prisoners the jailor must employ to identify the poisoned sweet?
Note: A sweet can be eaten by any number of prisoners.
 
Example 1:
Input:
N = 3
Output:
2
Explanation:
The poison can be identified using
only 2 prisoners.
Example 2:
Input:
N = 2
Output:
1
Explanation:
The poison can be identified using
only 1 prisoner.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numOfPrisoners() which takes an Integer N as input and returns the minimum number of prisoners required to identify the poisoned sweet.
 
Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{9}
"""

import math

def numOfPrisoners(N):
    if N == 1:
        return 0
    c = int(math.log2(N))
    if 2 ** c < N:
        c += 1
    return c