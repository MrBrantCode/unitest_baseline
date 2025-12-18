"""
QUESTION:
Given a positive integer N, find the last digit of the N^{th} term from the Fibonacci series.
Note: For N=0 you have to return 0.
 
Example 1:
Input:
N = 5
Output:
5
Explanation:
5th Fibonacci number is 5
Example 2:
Input:
N = 14
Output:
7
Explanation:
14th Fibonacci number is 377
It's last digit is 7
Your Task:
You don't need to read input or print anything. Your task is to complete the function fib() which takes an integer N as input parameter and returns the last digit of Nth Fibonacci number.
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 
Constraints:
0 <= N <= 1000
"""

def last_digit_of_fibonacci(N: int) -> int:
    if N == 0:
        return 0
    else:
        a = 0
        b = 1
        for _ in range(1, N):
            c = (a + b) % 10  # Only keep the last digit during the calculation
            a = b
            b = c
        return b