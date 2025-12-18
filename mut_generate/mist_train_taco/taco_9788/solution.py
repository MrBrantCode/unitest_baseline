"""
QUESTION:
Given a number n, find the value of below expression:
            f(n-1)*f(n+1) - f(n)*f(n)    where f(n) is n^{th} Fibonacci. 
 
Example 1:
Input : n = 5
Output: -1
Explanation: f(4) = 3, f(5) = 5
f(6) = 8. 3 * 8 - 5 * 5 = -1
Example 2:
Input: n = 3
Output: -1
Explanation: f(2) = 1, f(3) = 2
and f(4) = 3. 1 * 3 - 2 * 2 = -1
 
Your Task:
You don't need to read or print anything. Yous task is to complete the function evaluate_exp() which takes n as input parameter and returns the value of the given expression.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 10^{18}
"""

def evaluate_exp(n: int) -> int:
    if n & 1:
        return -1
    return 1