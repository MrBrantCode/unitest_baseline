"""
QUESTION:
Write a function `solve(arr)` that takes an integer array as input, segregates its elements into distinct categories: even, odd, prime, and non-prime (composite), and sorts each category in ascending order. Minimize the time complexity of the sorting algorithm used. The function `is_prime(n)` that checks whether a number is prime or not is also required.
"""

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def solve(arr):
    even = [i for i in arr if i % 2 == 0]
    odd = [i for i in arr if i % 2 != 0]
    prime = [i for i in arr if is_prime(i)]
    composite = [i for i in arr if not is_prime(i) and i != 1]

    even.sort()
    odd.sort()
    prime.sort()
    composite.sort()

    return even, odd, prime, composite