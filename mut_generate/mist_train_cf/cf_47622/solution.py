"""
QUESTION:
Implement a function called `multiply_by_primes` that takes an array of integers and multiplies each element by a unique prime number starting from the 1st prime number (2) for the first element, the 2nd prime number (3) for the second element, and so on. The function should return the new array. The function should be able to handle arrays of varying lengths, and it should generate enough prime numbers as needed.
"""

def multiply_by_primes(arr):
    def get_primes(n):
        numbers = set(range(n, 1, -1))
        primes = []
        while numbers:
            p = numbers.pop()
            primes.append(p)
            numbers.difference_update(set(range(p*2, n+1, p)))
        return primes

    primes = get_primes(100)  # Generate enough primes
    return [n * primes[i] for i, n in enumerate(arr)]