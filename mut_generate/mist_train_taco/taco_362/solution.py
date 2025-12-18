"""
QUESTION:
Given a positive integer N, The task is to find if it is a power of eight or not.
Example 1: 
Input: 64
Output: Yes
Explanation: 64 is power of 8.
Example 2:
Input: 75
Output: No
Explanation: 75 is not a power of 8.
Your Task:
You don't need to read or print anything. your task is to complete the function is_power_of_eight() which takes N as the input parameter and returns "Yes" if N is power of eight otherwise returns "No"(Wihtout quotes).
Expected Time Complexity: O(log(N))
Expected Space Complexity: O(1)
Constraints:
1 <= N <= 10^{18}
"""

def is_power_of_eight(n: int) -> str:
    (oc, zc) = (0, 0)
    while n != 0:
        if n & 1 == 0:
            zc += 1
        else:
            oc += 1
        n = n >> 1
    if oc == 1 and zc % 3 == 0:
        return 'Yes'
    return 'No'