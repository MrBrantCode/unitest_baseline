"""
QUESTION:
Given a number N, find whether N can be expressed as sum of two or more consecutive positive numbers. 
 
Example 1:
Input:
N = 10
Output:
Yes
Explanation:
10 can be expressesd as 1+2+3+4.
Example 2:
Input:
N = 8
Output:
No
Explanation:
8 can't be expressesd sum of two or
more consecutive numbers.
Example 3:
Input:
N = 24
Output:
Yes
Explanation:
24 can be expressesd as 7+8+9.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isSumOfConsecutive() which takes an Integer N as input and returns "Yes" and "No" accordingly.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def is_sum_of_consecutive(N: int) -> str:
    if N == 0:
        return 'Yes'
    while N != 1:
        if N % 2 != 0:
            return 'Yes'
        N = N // 2
    return 'No'