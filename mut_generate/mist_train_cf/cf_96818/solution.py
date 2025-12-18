"""
QUESTION:
Write a function `generate_prime_array(n, m)` that returns a 2-dimensional array of size n by m containing all prime numbers. The function should take two parameters, n and m, which are prime numbers greater than 2. If either n or m is not a prime number, the function should return None.
"""

def generate_prime_array(n, m):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if not (is_prime(n) and is_prime(m)):
        return None
    
    prime_array = []
    for i in range(n):
        row = []
        for j in range(m):
            num = i * m + j + 1
            if is_prime(num):
                row.append(num)
        prime_array.append(row)
    
    return prime_array