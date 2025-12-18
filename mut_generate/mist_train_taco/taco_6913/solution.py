"""
QUESTION:
We arrange the numbers between 1 and N (1 <= N <= 10000) in increasing order and decreasing order like this:


1 2 3 4 5 6 7 8 9 . . . N
N . . . 9 8 7 6 5 4 3 2 1


Two numbers faced each other form a pair. Your task is to compute the number of pairs P such that both numbers in the pairs are prime.



Input

Input contains several test cases. Each test case consists of an integer N in one line.

Output

For each line of input, output P .

Example

Input

1
4
7
51


Output

0
2
2
6
"""

def count_prime_pairs(n: int) -> int:
    # Sieve of Eratosthenes to find all primes up to 10000
    primes = [0, 0] + [1] * 9999
    for i in range(2, 101):
        if primes[i]:
            for j in range(i * i, 10001, i):
                primes[j] = 0
    
    # Generate the pairs and count the prime pairs
    prime_pairs_count = sum([1 for (a, b) in zip(range(1, n + 1), range(1, n + 1)[::-1]) if primes[a] and primes[b]])
    
    return prime_pairs_count