"""
QUESTION:
Given a number N, the task is to find the largest prime factor of that number.
 Example 1:
Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor i.e 5 only.
Example 2:
Input:
N = 24
Output:
3
Explanation:
24 has 2 prime factors 2 and 3 in which 3 is greater.
Your Task:
You don't need to read input or print anything. Your task is to complete the function largestPrimeFactor() which takes an integer N as input parameters and returns an integer, largest prime factor of N.
Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)
Constraints:
2 <= N <= 10^{9}
"""

def largest_prime_factor(N: int) -> int:
    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(N, 1, -1):
        if N % i == 0 and is_prime(i):
            return i