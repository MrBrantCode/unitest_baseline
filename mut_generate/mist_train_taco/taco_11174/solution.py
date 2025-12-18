"""
QUESTION:
Given N, check whether it is a Narcissistic number or not.
Note: Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits
 
Example 1:
Input:
N = 407
Output:
1
Explanation:
4^{3}+0^{3}+7^{3} = 64+0+343 
= 407 equals to N.
Example 2:
Input:
N = 111
Output:
0
Explanation:
1^{3}+1^{3}+1^{3} = 1+1+1
= 3 not equals to N.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isNarcissistic() which takes an integer N as input parameters and returns an integer, 1 if N is a narcissistic number or 0 otherwise.
 
Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def is_narcissistic(N: int) -> int:
    p = len(str(N))
    sum = 0
    temp = N
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** p
        temp //= 10
    
    if sum == N:
        return 1
    else:
        return 0