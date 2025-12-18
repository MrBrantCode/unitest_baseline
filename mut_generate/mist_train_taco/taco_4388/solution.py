"""
QUESTION:
Given a positive integer n. Find whether a number is a semiprime or not.
 Note: A semiprime is a natural number that is a product of two prime numbers .
Example 1:
Input:
N=35
Output:
1
Explanation:
35=7x5.So 35 is a semi-prime.
Example 2:
Input:
8
Output:
0
Explanation:
8 is not a semi prime.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function checkSemiprime() which takes a number N as input parameter and returns 1 if it is a semi prime number.Otherwise, it returns 0.
Expected Time Complexity:O(Sqrt(N))
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{9}
"""

import math

def is_semiprime(n: int) -> int:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i) and is_prime(n // i):
                return 1
    return 0