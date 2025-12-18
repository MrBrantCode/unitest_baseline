"""
QUESTION:
Given a number N, you have to say if it is adjacent to two prime numbers. Two numbers are adjacent if the absolute difference between them is 1.
Example 1:
Input: N = 4
Output: Y
Explaination: The adjacent numbers 3 and
 5 are both prime.
Eaxmple 2:
Input: 7
Output: N
Explaination: The numbers 6 and 8 are 
not prime.
Your Task:
You do not need to read input or print anything. Your task is to complete the function primeAdjacent() which takes N as input parameter and reutrns 1 if it has two adjacent prime numbers, otherwise, returns 0.
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
2 ≤ N ≤ 5000
"""

def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def is_adjacent_to_primes(N):
    ans1 = is_prime(N + 1)
    ans2 = is_prime(N - 1)
    return ans1 and ans2