"""
QUESTION:
Given a positive integer N, write a function to find if it is a power of three or not.
 
Example 1:
Input:
N = 3
Output:
Yes
Explanation:
3^{1} is a power of 3.
 
Example 2:
Input:
N = 5
Output:
No
Explanation:
5 is not a power of 3.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isPowerof3() which takes an integer N and returns "Yes" if N is a power of 3, else "No" if N is not a power of 3.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=N<=(32-bit largest integer)
"""

import math

def is_power_of_three(N: int) -> str:
    if N > 0 and 3 ** round(math.log(N, 3)) == N:
        return 'Yes'
    return 'No'