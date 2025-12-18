"""
QUESTION:
Write a function `find_primes(n: int) -> List[int]` that returns an array with all the prime numbers between 2 and `n`, inclusive. The input parameter `n` is a positive integer where 2 <= n <= 10^6. The solution should have a time complexity of O(n*log(log(n))) or better, and should be implemented in a single function without any helper functions or additional data structures. Handle the case when `n` is equal to 2 separately and return `[2]` as the output.
"""

def find_primes(n: int) -> list[int]:
    """Returns an array with all the prime numbers between 2 and n, inclusive."""
    if n == 2:
        return [2]

    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    # Iterate from 2 to sqrt(n)
    for p in range(2, int(n ** 0.5) + 1):
        # If p is a prime, mark as composite all the multiples of p
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    # Return a list of all prime numbers in the range
    return [p for p in range(2, n + 1) if prime[p]]