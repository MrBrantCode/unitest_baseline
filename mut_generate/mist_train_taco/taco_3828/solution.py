"""
QUESTION:
Given a number positive number N, find value of f_{0} + f_{1} + f_{2} + . + f_{N} where f_{i} indicates ith Fibonacci number.
Remember that f_{0} = 0, f_{1} = 1, f_{2} = 1, f_{3} = 2, f_{4} = 3, f_{5} = 5, 
Since the answer can be very large, answer modulo 1000000007 should be returned.
Example 1:
Input:
N = 3
Output:
4
Explanation:
0 + 1 + 1 + 2  = 4
Example 2:
Input :
N = 4
Output :
7
Explanation :
0 + 1 + 1 + 2 + 3 = 7
Your Task:
You don't need to read input or print anything. Your task is to complete the function fibSum() which takes an integer N as input parameter and returns the sum of all the Fibonacci number from F_{0} to F_{N}.
Expected Time Complexity: O(Log N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 100000
"""

def fibonacci_sum(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    MOD = 1000000007
    a, b = 0, 1
    fib_sum = 1  # Starting with F_1 = 1
    
    for i in range(2, N + 1):
        a, b = b, (a + b) % MOD
        fib_sum = (fib_sum + b) % MOD
    
    return fib_sum