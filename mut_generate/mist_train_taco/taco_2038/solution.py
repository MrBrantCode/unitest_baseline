"""
QUESTION:
A greek once sifted some numbers. And it did something wonderful!

-----Input:-----
- First line will contain an integer $N$

-----Output:-----
Output in a single line answer to the problem.

-----Constraints-----
- $1 \leq N \leq 10^5$

-----Sample Input 1:-----
10

-----Sample Output 1:-----
4

-----Sample Input 2:-----
20

-----Sample Output 2:-----
8
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def count_primes_up_to(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count