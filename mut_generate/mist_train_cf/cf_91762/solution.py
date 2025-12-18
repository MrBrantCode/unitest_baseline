"""
QUESTION:
Implement a function named `sum_of_primes` that takes an integer `n` as input and prints the sum of all prime numbers up to `n`. The function must have a time complexity of O(n log(log n)) and cannot use any external libraries or built-in functions to check for prime numbers.
"""

def sum_of_primes(n):
    if n < 2:
        print("No prime numbers up to", n)
        return
    primes = [2]
    prime_sum = 2
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
            prime_sum += num
    print("Sum of prime numbers up to", n, ":", prime_sum)