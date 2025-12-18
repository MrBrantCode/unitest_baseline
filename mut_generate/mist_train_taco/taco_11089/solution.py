"""
QUESTION:
Given an array of length N, starting from 1 to N. At each iteration, you remove all elements at odd positions, until only one element is left. Find the last remaining element.
 
Example 1:
Input:
N = 5
Output:
4
Explanation:
Initial Array- {1,2,3,4,5}.
After 1st Iteration- {2,4}.
After 2nd Interation- {4}
Threfore, the answer is 4.
Example 2:
Input:
N = 3
Output:
2
Explanation:
Initial Array- {1,2,3}.
After 1st Iteration- {2}.
Threfore, the answer is 2.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function oddGame() which takes an Integer N as input and returns the last remaining element.
 
Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{9}
"""

import math

def find_last_remaining_element(N: int) -> int:
    if N == 1:
        return 1
    c = int(math.log2(N))
    return 1 << c