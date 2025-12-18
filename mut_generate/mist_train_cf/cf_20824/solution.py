"""
QUESTION:
Write a function named `fibonacci_prime_numbers` that takes a positive integer `N` as input and prints the first N prime numbers in a Fibonacci series. The function should have a time complexity of O(NlogN) and a space complexity of O(N).
"""

def fibonacci_prime_numbers(N):
    if N <= 0:
        print("Invalid input! N should be a positive integer.")
        return
    if N == 1:
        print(2)
        return
    if N == 2:
        print(2)
        print(3)
        return
    prime_numbers = [2, 3]
    count = 2
    i = 4
    while count < N:
        if is_prime(i):
            prime_numbers.append(i)
            count += 1
        i += 1
    fib_numbers = [0, 1]
    for i in range(2, N + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    for i in range(N):
        print(fib_numbers[i], prime_numbers[i])

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True