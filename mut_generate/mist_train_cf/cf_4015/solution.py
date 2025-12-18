"""
QUESTION:
Generate a list of the square of all prime numbers between 1 and a given number 'n' using the Sieve of Eratosthenes algorithm, with a time complexity of O(n*log(log(k))), where 'k' is the largest prime number between 1 and 'n'.
"""

def entrance(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [i * i for i in range(2, n+1) if is_prime[i]]