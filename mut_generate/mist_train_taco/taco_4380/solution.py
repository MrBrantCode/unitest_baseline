"""
QUESTION:
You will be given two positive numbers M and N. Your task is to print the greatest common divisor of Fib(M) and Fib(N) where Fib(x) means the x'th Fibonacci numbers defined as:
Fib(0) = 0
Fib(1) = 1
for n > 1, Fib(n) = Fib(n-1) + Fib(n-2)
Example 1:
Input: M = 3, N = 6
Output: 2
Explanation: Fib(3) = 2 and Fib(6) = 8
So, GCD(2,8)%100 = 2
Ã¢â¬â¹Example 2:
Input: M = 7, N = 8
Output: 1
Explanation: Fib(7) = 13 and Fib(8) = 21
So, GCD(13,21)%100 = 1
Your Task:  
You don't need to read input or print anything. Your task is to complete the function fibGcd() which takes M and N as inputs and returns the answer.The answer may be very large, compute the answer modulo 100.
Expected Time Complexity: O(min(M, N))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ M, N ≤ 10^{3}
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def fib_gcd(M, N):
    fib_M = fib(M)
    fib_N = fib(N)
    result_gcd = gcd(fib_M, fib_N)
    return result_gcd % 100