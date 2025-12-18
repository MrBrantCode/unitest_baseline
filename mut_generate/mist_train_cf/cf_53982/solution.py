"""
QUESTION:
Write a function `print_prime_and_sum` that takes two integers `start` and `end` as input, prints all prime numbers between `start` and `end` (inclusive), and calculates the sum of their digits using recursive functions. The function should not take any other parameters besides `start` and `end`, and should not return any value.
"""

def is_prime(n, i=2):
    if n <= 2:
        if n == 2:
            return True
        else:
            return False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def summation(n):
    if n == 0:
        return 0
    else:
        return n%10 + summation(n//10)

def print_prime_and_sum(start, end):
    if start > end:
        return
    else:
        if is_prime(start):
            print(f"Prime: {start}, Sum: {summation(start)}")
        print_prime_and_sum(start+1, end)