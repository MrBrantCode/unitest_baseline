"""
QUESTION:
Create a function `find_numbers(N)` that takes an integer `N` as input and returns two lists: one containing all prime numbers ranging from 2 to `N`, and another containing the prime numbers from the first list that are also 'happy numbers'. A happy number is defined as a number that eventually reaches 1 when replaced by the sum of the square of its digits, repeating this process until the number equals 1 or enters a cycle that does not include 1.
"""

def find_numbers(N):
    def is_prime(n):
        if n <= 1:
            return False
        if n <=3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_happy(n):
        visited = set()
        while n != 1 and not n in visited:
            visited.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1

    primes = [i for i in range(2, N+1) if is_prime(i)]
    happy_primes = [i for i in primes if is_happy(i)]
    return primes, happy_primes