"""
QUESTION:
Create a function `generate_prime_array` that takes two parameters, n and m, both of which are prime numbers greater than 2. The function should return a 2-dimensional array of size n by m, where each element is a prime number, starting from 2 and increasing. If n or m is not a prime number, the function should return None.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_array(n, m):
    if not (is_prime(n) and is_prime(m)):
        return None
    
    prime_array = []
    num = 1
    for i in range(n):
        row = []
        for j in range(m):
            num += 1
            while not is_prime(num):
                num += 1
            row.append(num)
        prime_array.append(row)
    
    return prime_array