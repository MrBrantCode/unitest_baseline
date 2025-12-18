"""
QUESTION:
Write a function called `are_relatively_prime` that takes two integers `a` and `b` as input and returns a boolean indicating whether they are relatively prime. The function should also output the prime factorization of `a` and `b` and the number of distinct prime factors they share. The function should use recursion and should not use any external libraries or built-in prime factorization functions.
"""

def are_relatively_prime(a, b):
    def prime_factors(n, factors=set()):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                factors.add(i)
                return prime_factors(n//i, factors)
        if n > 1:
            factors.add(n)
        return factors

    a_factors = prime_factors(a)
    b_factors = prime_factors(b)
    shared_factors = a_factors.intersection(b_factors)

    print(f"{a} prime factors: {a_factors}")
    print(f"{b} prime factors: {b_factors}")
    print(f"Number of distinct prime factors shared by {a} and {b}: {len(shared_factors)}")
    return len(shared_factors) == 0