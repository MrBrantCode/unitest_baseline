"""
QUESTION:
Create a function `print_prime_table` that takes no arguments and prints a prime number table up to a limit, where the limit is a prime Fibonacci number that is also a palindrome. The function should find the nearest prime Fibonacci number that is also a palindrome, starting from the value 313, and then print the prime number table up to that limit, with the prime numbers displayed in both ascending and descending orders.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def print_prime_table():
    table_limit = 313
    n = table_limit
    while True:
        if is_fibonacci(n) and is_palindrome(n) and is_prime(n):
            break
        n -= 1

    print("Prime number table up to", n)
    print("----------------------------")
    print("Prime Number\t\tPrime Number")
    print("in Ascending Order\tin Descending Order")
    print("----------------------------")

    prime_numbers = [i for i in range(2, n+1) if is_prime(i)]
    for i in range(len(prime_numbers)):
        print(f"{prime_numbers[i]}\t\t\t{prime_numbers[-i-1]}")