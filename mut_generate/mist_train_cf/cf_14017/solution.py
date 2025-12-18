"""
QUESTION:
Write a function `generate_prime_array(n, m)` that returns a 2-dimensional array of size n by m containing all prime numbers starting from the first prime number, 2, and fill the array row by row. The function should not take any other input other than n and m, and should be able to handle any positive integer values of n and m.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def entrance(n, m):
    prime_array = []
    num = 2
    while len(prime_array) < n * m:
        if is_prime(num):
            prime_array.append(num)
        num += 1
    
    prime_array_2d = []
    for i in range(n):
        prime_array_2d.append([])
        for j in range(m):
            prime_array_2d[i].append(prime_array[i * m + j])
    
    return prime_array_2d