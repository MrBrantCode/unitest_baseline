"""
QUESTION:
Given a positive integer N, find if it can be expressed as x^{y} where y > 1 and x > 0 and x and y both are both integers.
 
Example 1:
Input:
N = 8
Output:
1
Explanation:
8 can be expressed
as 2^{3}.
 
 
Example 2:
Input:
N = 7
Output:
0
Explanation:
7 can't be expressed
int the form x^{y}.
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function checkPower() which takes an integer N and returns 1 if possible else, 0.
 
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1<= N <=10000
"""

def can_be_expressed_as_power(N: int) -> int:
    if N <= 1:
        return 1
    
    n = 2
    while n <= (N ** 0.5):
        t = n * n
        while t <= N:
            if t == N:
                return 1
            t *= n
        n += 1
    
    return 0