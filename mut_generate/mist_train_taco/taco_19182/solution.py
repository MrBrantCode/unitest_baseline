"""
QUESTION:
Given a positive integer N and a prime p, the task is to print the largest power of prime p that divides N!. Here N! means the factorial of N = 1 x 2 x 3 . . (N-1) x N.
Note that the largest power may be 0 too.
 
Example 1:
Input:
N = 5 , p = 2
Output:
3
Explanation:
5! = 120. The highest x for which 2^{x}
divides 120 is 3, as 120%8 = 0.
So, the Output is 3.
Example 2:
Input:
N = 3 , p = 5
Output:
0
Explanation:
3! = 6. The highest x for which 5^{x}
divides 6 is 0, as 6%1 = 0.
So, the Output is 0.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function largestPowerOfPrime() which takes 2 Integers N and p as input and returns the answer.
 
Expected Time Complexity: O(log_{p}(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
2 <= p <= 5000
"""

def largest_power_of_prime(N: int, p: int) -> int:
    sum = 0
    while N:
        N //= p
        sum += N
    return sum